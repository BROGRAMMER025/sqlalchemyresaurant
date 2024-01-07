# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    def reviews(self):
        return [f"Review for {self.name} by {review.customer().full_name()}: {review.star_rating} stars." for review in self.review]

    def customers(self):
        return [review.customer() for review in self.review]

    @classmethod
    def fanciest(cls):
        return cls.query.order_by(cls.price.desc()).first()

    @classmethod
    def all_reviews(cls):
        return [review.full_review() for review in cls.query.join(Review).filter(Review.restaurant_id == cls.id).all()]

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def reviews(self):
        return [f"Review for {review.restaurant().name} by {self.full_name()}: {review.star_rating} stars." for review in self.review]

    def restaurants(self):
        return [review.restaurant() for review in self.review]

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        return max(self.review, key=lambda review: review.star_rating).restaurant()

    def add_review(self, restaurant, rating):
        new_review = Review(restaurant=restaurant, customer=self, star_rating=rating)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant):
        session.query(Review).filter(Review.customer_id == self.id, Review.restaurant_id == restaurant.id).delete()
        session.commit()

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    def customer(self):
        return session.query(Customer).get(self.customer_id)

    def restaurant(self):
        return session.query(Restaurant).get(self.restaurant_id)

    def full_review(self):
        return f"Review for {self.restaurant().name} by {self.customer().full_name()}: {self.star_rating} stars."

# Create an engine and bind it to the Base class
engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
