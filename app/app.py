#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request, jsonify
from flask_migrate import Migrate

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    result = [{"id": restaurant.id, "name": restaurant.name, "address": restaurant.address} for restaurant in restaurants]
    return jsonify(result)


@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        pizzas = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in restaurant.pizzas]
        result = {"id": restaurant.id, "name": restaurant.name, "address": restaurant.address, "pizzas": pizzas}
        return jsonify(result)
    else:
        return jsonify({"error": "Restaurant not found"}), 404
    
    
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        RestaurantPizza.query.filter_by(restaurant_id=id).delete()
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({"error": "Restaurant not found"}), 404
    
    
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    result = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in pizzas]
    return jsonify(result)

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get("price")
    pizza_id = data.get("pizza_id")
    restaurant_id = data.get("restaurant_id")

    if not (price and pizza_id and restaurant_id):
        return jsonify({"errors": ["validation errors"]}), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not (pizza and restaurant):
        return jsonify({"errors": ["validation errors"]}), 400

    restaurant_pizza = RestaurantPizza(price=price, restaurant=restaurant, pizza=pizza)
    db.session.add(restaurant_pizza)
    db.session.commit()

    return jsonify({"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients}), 201


if __name__ == '__main__':
    app.run(port=5555, debug=True)



