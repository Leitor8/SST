from flask import Flask, request, jsonify, make_response
from mvc_flask import FlaskMVC
from flask_sqlalchemy import SQLAlchemy
from os import environ



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')

    FlaskMVC(app)
    
    return app


app = create_app()
db = SQLAlchemy(app=app)



from app.models.orders import Order
from app.controllers.order_controller import OrderController

with app.app_context():
    db.create_all()
    db.session.commit()