import logging
from app.models.orders import Order
from app.services.consumer_service import ConsumerService
from app.services.producer_service import ProducerService

class OrderController:
    def index(self):
        return ''