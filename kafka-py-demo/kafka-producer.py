from confluent_kafka import Producer

# Configure Kafka connection
bootstrap_servers = 'localhost:9092'  # Replace with your Kafka broker address

# Create a Kafka producer configuration
producer_config = {
    'bootstrap.servers': bootstrap_servers,
    'client.id': 'my-producer'
}

# Create a Kafka producer instance
producer = Producer(producer_config)

# Produce a message to a topic
topic = 'my-topic'
key = 'my-key'  # Optional: Set a message key
value = 'Hello, Kafka!'

producer.produce(topic, key=key, value=value)
producer.flush()

print(f"Produced message: {value} to topic: {topic}")