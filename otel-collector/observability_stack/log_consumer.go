package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"

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
	groupID := "log-consumer-group"

	r := kafka.NewReader(kafka.ReaderConfig{
		Brokers:  []string{kafkaURL},
		Topic:    topic,
		GroupID:  groupID,
		MinBytes: 1e3,  // 1KB
		MaxBytes: 10e6, // 10MB
	})
	defer r.Close()

	fmt.Println("Consumer started...")

	for {
		m, err := r.ReadMessage(context.Background())
		if err != nil {
			log.Println("Error reading message:", err)
			continue
		}

		var logEntry LogEntry
		err = json.Unmarshal(m.Value, &logEntry)
		if err != nil {
			log.Println("Error parsing message:", err)
			continue
		}

		fmt.Printf("Received: %s [%s] %s\n", logEntry.Timestamp, logEntry.Level, logEntry.Message)
	}
}
