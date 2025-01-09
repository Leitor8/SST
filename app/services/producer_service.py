from kafka import KafkaProducer

class ProducerService:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def send_message(self, topic_name, key, value):
        try:
            self.producer.send(topic_name, key=key, value=value)
            self.producer.flush()
            print('Mensagem enviada com sucesso!')
        except Exception as ex:
            print('Erro ao enviar mensagens.')
            print(ex)

    def __del__(self):
        self.producer.close()
