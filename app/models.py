from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates


 
db = SQLAlchemy()


# Models
class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', back_populates='restaurants')

class Pizza(db.Model):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizza', back_populates='pizzas')


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurantpizzas'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id')) 
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))  
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    @validates('price')
    def validate_price(self, key, value):
        if not (200 <= value <= 2500):
            raise ValueError("Price must be between 200 and 2500.")
        return value
