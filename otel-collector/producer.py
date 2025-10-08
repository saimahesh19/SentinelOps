from kafka import KafkaProducer
import random
import time
import json
from datetime import datetime

# Pre-loaded dataset from your analysis
log_data = {
    "INFO": {
        "components": [
            "SecurityLogger.org.apache.hadoop.ipc.Server",
            "org.apache.hadoop.http.HttpRequestLog",
            "org.apache.hadoop.mapreduce.v2.app.MRAppMaster",
            "org.apache.hadoop.mapreduce.v2.app.job.impl.TaskImpl",
            "org.apache.hadoop.yarn.event.AsyncDispatcher"
        ],
        "templates": [
            "Created MRAppMaster for application appattempt_<*>",
            "Connecting to ResourceManager at <*>/<*>:<*>",
            "Attempt_<*> TaskAttempt Transitioned from NEW to RUNNING",
            "Http request log for http.requests.mapreduce is not defined"
        ]
    },
    "WARN": {
        "components": [
            "org.apache.hadoop.hdfs.DFSClient",
            "org.apache.hadoop.ipc.Client"
        ],
        "templates": [
            "DFSOutputStream ResponseProcessor exception for block BP-<*>:blk_<*>",
            "Task cleanup failed for attempt attempt_<*>"
        ]
    },
    "ERROR": {
        "components": [
            "org.apache.hadoop.mapreduce.jobhistory.JobHistoryEventHandler",
            "org.apache.hadoop.yarn.YarnUncaughtExceptionHandler"
        ],
        "templates": [
            "ERROR IN CONTACTING RM.",
            "Error writing History Event: org.apache.hadoop.mapreduce.jobhistory.TaskAttemptUnsuccessfulCompletionEvent@<*>"
        ]
    },
    "FATAL": {
        "components": [
            "org.apache.hadoop.mapred.TaskAttemptListenerImpl"
        ],
        "templates": [
            "Task: attempt_<*> - exited : java.net.NoRouteToHostException"
        ]
    }
}

# Kafka setup
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)



topic = "logs-topic"

def fill_placeholders(template):
    """Replace <*> placeholders with random realistic values."""
    while "<*>" in template:
        replacement = str(random.choice([
            f"job_{random.randint(1000,9999)}",
            f"attempt_{random.randint(10000,99999)}",
            f"{random.randint(100,999)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
            random.randint(1024,65535),
            f"memory:{random.randint(1024,32768)}, vCores:{random.randint(1,8)}"
        ]))
        template = template.replace("<*>", replacement, 1)
    return template

while True:
    # Pick random log level
    level = random.choice(list(log_data.keys()))
    comp = random.choice(log_data[level]["components"])
    template = random.choice(log_data[level]["templates"])
    message = fill_placeholders(template)

    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "level": level,
        "component": comp,
        "message": message
    }

    producer.send(topic, log_entry)
    print(f"Sent: {log_entry}")
    time.sleep(1)

