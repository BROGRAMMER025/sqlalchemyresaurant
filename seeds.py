# seeds.py
from models import Restaurant, Customer, Review, session

def create_sample_data():
    # Create restaurants
    restaurant1 = Restaurant(name='Restaurant A', price=3)
    restaurant2 = Restaurant(name='Restaurant B', price=4)
    restaurant3 = Restaurant(name='Restaurant C', price=2)

    session.add_all([restaurant1, restaurant2, restaurant3])
    session.commit()

    # Create customers
    customer1 = Customer(first_name='John', last_name='Doe')
    customer2 = Customer(first_name='Jane', last_name='Smith')
    customer3 = Customer(first_name='Bob', last_name='Johnson')

    session.add_all([customer1, customer2, customer3])
    session.commit()

    # Create reviews
    review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
    review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)
    review3 = Review(star_rating=3, restaurant=restaurant3, customer=customer3)

    session.add_all([review1, review2, review3])
    session.commit()

if __name__ == '__main__':
    create_sample_data()
