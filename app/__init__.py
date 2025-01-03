from flask import Flask, request, jsonify, make_response
from mvc_flask import FlaskMVC
from flask_sqlalchemy import SQLAlchemy
from os import environ

def create_app():
    app = Flask(__name__)

    FlaskMVC(app)

    return app

app = create_app()


# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')

# db = SQLAlchemy(app)

# class Order(db.Model):
#     __tablename__ = 'orders'

#     id = db.Column(db.Integer, primary_key = True)

#     def json(self):
#         return {'id': id}

# db.create_all()

# @app.route('/test', methods=['GET'])
# def test():
#     return make_response(jsonify({'message': 'test route'}), 200)

# @app.route('/orders/<int:id>', methods=['GET'])
# def get_order(id):
#     try:
#         order = Order.query.filter_by(id=id).first()
#         return make_response(jsonify({'order': order.json()}), 200)
#     except:
#         return make_response(jsonify({'message': 'Error getting order'}, 500))
    
# @app.route('/logs', methods=['GET'])
# def get_logs():
#     try:
#         return make_response(jsonify({'message': 'logs'}), 200)
#     except:
#         return make_response(jsonify({'message': 'Error getting logs'}), 500)