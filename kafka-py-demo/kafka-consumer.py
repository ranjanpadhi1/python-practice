from confluent_kafka import Consumer, KafkaError

# Configure Kafka connection
bootstrap_servers = 'localhost:9092'  # Replace with your Kafka broker address

# Create a Kafka consumer configuration
consumer_config = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'my-consumer-group',  # Specify your consumer group
    'auto.offset.reset': 'earliest'  # Start consuming from the beginning of the topic
}

# Create a Kafka consumer instance
consumer = Consumer(consumer_config)

# Subscribe to a topic
topic = 'my-topic'
consumer.subscribe([topic])

# Consume messages
while True:
    msg = consumer.poll(1.0)  # Adjust the timeout as needed
    if msg is None:
        continue
    if msg.error():
        print(f"Error: {msg.error()}")
    else:
        print(f"Consumed message: {msg.value().decode('utf-8')}")

# Close the consumer gracefully
consumer.close()