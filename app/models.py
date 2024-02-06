from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin


 
db = SQLAlchemy()


# Models

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    restaurantspizzas = db.relationship("RestaurantPizza", backref='restaurants')  
    pizzas= db.relationship("Pizza", secondary='restaurantspizzas', backref='restaurants', viewonly=True)
    serialize_rules = ('-restaurantspizzas.restaurant',)


class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at =db.Column(db.DateTime, server_default=db.func.now())

    restaurantspizzas = db.relationship("RestaurantPizza", backref='pizzas')  
    serialize_rules = ('-restaurantspizzas.pizza',)


class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurantspizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer())
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

  
    serialize_rules = ('-restaurant', '-pizza')
  
    @validates('price')
    def validate_price(self, key, value):
        if not (0 <= value <= 30):
            raise ValueError("Price must be between 0 and 30.")
        return value