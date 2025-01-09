from kafka import KafkaConsumer

class ConsumerService:
    def __init__(self, topic_name):
        self.consumer = KafkaConsumer(
            bootstrap_servers='localhost:9092',
            max_poll_records=10,
            auto_offset_reset='earliest',
            session_timeout_ms=6000,
            heartbeat_interval_ms=3000
        )
        self.consumer.subscribe(topics=[topic_name])

    def consume_msg(self):
        for message in self.consumer:
            print(message.value)
            yield [
                message.value["timestamp"],
                message.value["order_id"],
                message.value["customer_id"],
                message.value["product_id"],
                message.value["quantity"],
                message.value["price"]
            ]

    def __del__(self):
        self.consumer.close()