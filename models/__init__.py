from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .order import OrderModel
from .product import ProductModel
from .user import UserModel
