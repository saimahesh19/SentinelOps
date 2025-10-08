package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"time"
	"github.com/segmentio/kafka-go"
)

type LogEntry struct {
	Timestamp  string            `json:"timestamp"`
	Level      string            `json:"level"`
	AppName    string            `json:"app_name"`
	InstanceID string            `json:"instance_id"`
	Message    string            `json:"message"`
	Tags       map[string]string `json:"tags,omitempty"`
}

func main() {
	kafkaURL := "localhost:9092"
	topic := "app-logs"

	writer := kafka.NewWriter(kafka.WriterConfig{
		Brokers:  []string{kafkaURL},
		Topic:    topic,
		Balancer: &kafka.LeastBytes{},
	})
	defer writer.Close()

	var batch []kafka.Message
	batchSize := 3
	retryInterval := time.Second * 2

	for i := 1; i <= 10; i++ {
		logEntry := createLog(i)
		if !filterLog(logEntry) {
			continue
		}
		enrichLog(&logEntry)

		jsonData, err := json.Marshal(logEntry)
		if err != nil {
			log.Println("Serialization error:", err)
			continue
		}

		msg := kafka.Message{
			Key:   []byte(fmt.Sprintf("key-%d", i)),
			Value: jsonData,
		}

		batch = append(batch, msg)

		if len(batch) >= batchSize {
			sendBatchWithRetry(writer, batch, retryInterval)
			batch = nil
		}
		time.Sleep(500 * time.Millisecond)
	}

	// Send remaining messages if any
	if len(batch) > 0 {
		sendBatchWithRetry(writer, batch, retryInterval)
	}
}

func createLog(i int) LogEntry {
	level := "INFO"
	if i%3 == 0 {
		level = "ERROR"
	}
	return LogEntry{
		Timestamp:  time.Now().UTC().Format(time.RFC3339),
		Level:      level,
		AppName:    "payment-service",
		InstanceID: "instance-01",
		Message:    fmt.Sprintf("Log message number %d", i),
		Tags:       make(map[string]string),
	}
}

func filterLog(log LogEntry) bool {
	return log.Level == "ERROR" || log.Level == "WARN"
}

func enrichLog(log *LogEntry) {
	log.Tags["env"] = "staging"
	log.Tags["region"] = "us-east-1"
}

func sendBatchWithRetry(writer *kafka.Writer, batch []kafka.Message, retryInterval time.Duration) {
	maxRetries := 3
	for attempt := 1; attempt <= maxRetries; attempt++ {
		err := writer.WriteMessages(context.Background(), batch...)
		if err != nil {
			log.Printf("Attempt %d failed to send batch: %v\n", attempt, err)
			time.Sleep(retryInterval)
		} else {
			log.Printf("Batch sent successfully with %d messages\n", len(batch))
			return
		}
	}
	log.Println("Failed to send batch after retries")
}
