from app import db

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key = True)
    customerId = db.Column(db.Integer, nullable = False)
    items = db.Column(db.String)
    total = db.Column(db.Float, nullable = False)

    def json(self):
        return {'id': self.id, 'customerId': self.customerId, 'items': self.items, 'total': self.total}