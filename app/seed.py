from models import db, Restaurant, Pizza, RestaurantPizza
from app import app

def seed_data():
    with app.app_context():

        # Create restaurants
        restaurant1 = Restaurant(name='Restaurant 1', address='123 Main St')
        restaurant2 = Restaurant(name='Restaurant 2', address='456 Elm St')

        # Create pizzas
        pizza1 = Pizza(name='Margherita', ingredients='Tomato, Mozzarella, Basil')
        pizza2 = Pizza(name='Pepperoni', ingredients='Tomato, Mozzarella, Pepperoni')


        # Create restaurant pizzas (associations between restaurants and pizzas with prices)
        restaurant_pizza1 = RestaurantPizza(price=12.99, restaurant_id=restaurant1.id, pizza_id=pizza1.id)
        restaurant_pizza2 = RestaurantPizza(price=15.99, restaurant_id=restaurant1.id, pizza_id=pizza2.id)
        restaurant_pizza3 = RestaurantPizza(price=11.99, restaurant_id=restaurant2.id, pizza_id=pizza1.id)
        restaurant_pizza4 = RestaurantPizza(price=14.99, restaurant_id=restaurant2.id, pizza_id=pizza2.id)

        # Add restaurant pizzas restaurants and pizzas to database
       
        db.session.add_all([restaurant1, restaurant2, pizza1, pizza2,restaurant_pizza1, restaurant_pizza2, restaurant_pizza3, restaurant_pizza4])
        db.session.commit()

if __name__ == '__main__':
    seed_data()
