from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Enum
from app import db, app
import hashlib
from enum import Enum as RoleEnum
from flask_login import UserMixin


class UserRole(RoleEnum):
    ADMIN = 1
    USER = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100), nullable=True)
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    active = Column(Boolean, default=True)
    image = Column(String(100), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name



if __name__ == '__main__':
    with app.app_context():
        db.create_all()


        # u = User(name="admin", username="admin", password=str(hashlib.md5("123456".encode('utf-8')).hexdigest()),
        #          avatar="https://cdnv2.tgdd.vn/mwg-static/common/News/1569924/9.jpg",
        #          user_role=UserRole.ADMIN)
        # db.session.add(u)
        # db.session.commit()

        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()

        # data = [{
        #     "id": 1,
        #     "name": "iPhone 7 Plus",
        #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #     "price": 17000000,
        #     "image": "https://cdnv2.tgdd.vn/mwg-static/common/News/1569924/9.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 2,
        #     "name": "iPad Pro 2021",
        #     "description": "Apple, 128GB, RAM: 6GB",
        #     "price": 37000000,
        #     "image": "https://cdnv2.tgdd.vn/mwg-static/common/News/1569924/9.jpg",
        #     "category_id": 2
        # }, {
        #     "id": 3,
        #     "name": "Galaxy Note 11 Plus",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image": "https://cdnv2.tgdd.vn/mwg-static/common/News/1569924/9.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 4,
        #     "name": "Galaxy Note 13 Pro",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 45000000,
        #     "image": "https://cdnv2.tgdd.vn/mwg-static/common/News/1569924/9.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 4,
        #     "name": "Galaxy Note 18 Plus",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image": "https://cdnv2.tgdd.vn/mwg-static/common/News/1569924/9.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 5,
        #     "name": "Redmi Note 13",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 15000000,
        #     "image": "https://cdnv2.tgdd.vn/mwg-static/common/News/1569924/9.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 6,
        #     "name": "Xiaomi Poco a67 ",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 17000000,
        #     "image": "https://cdnv2.tgdd.vn/mwg-static/common/News/1569924/9.jpg",
        #     "category_id": 1
        # }]
        #
        # for p in data:
        #     prod = Product(name=p['name'], description=p['description'], price=p['price'],
        #                    image=p['image'], category_id=p['category_id'])
        #     db.session.add(prod)
        # db.session.commit()
