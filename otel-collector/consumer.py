from kafka import KafkaConsumer
import requests
import json
from datetime import datetime

# Load configuration from config.json
with open('config.json') as f:
    config = json.load(f)

# Extract Kafka settings
kafka_config = config["kafka"]
loki_config = config["loki"]
log_stream = config["log_stream"]

# Initialize Kafka consumer
consumer = KafkaConsumer(
    kafka_config["topic"],
    bootstrap_servers=kafka_config["bootstrap_servers"],
    auto_offset_reset=kafka_config["auto_offset_reset"],
    group_id=kafka_config["group_id"],
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

def push_to_loki(log):
    """Push a single log entry to Loki."""
    ts_ns = int(datetime.utcnow().timestamp() * 1e9)  # nanoseconds
    stream = {
        "stream": {
            "level": log.get("level", log_stream["default_level"]),
            "component": log.get("component", log_stream["default_component"])
        },
        "values": [
            [str(ts_ns), log.get("message", "")]
        ]
    }
    payload = {"streams": [stream]}
    try:
        r = requests.post(loki_config["url"], json=payload)
        if r.status_code != 204:
            print(f"❌ Loki error {r.status_code}: {r.text}")
    except Exception as e:
        print("⚠️ Loki push failed:", e)

print("✅ Loki consumer listening...")
for msg in consumer:
    log = msg.value
    print(f"→ Sending to Loki: {log}")
    push_to_loki(log)
