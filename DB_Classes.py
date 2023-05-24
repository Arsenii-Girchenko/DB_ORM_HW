import psycopg2
import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=100), unique=True)

class Book(Base):
    __tablename__ = 'book'
    
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=100), unique=True)
    id_publiher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'))

class Shop(Base):
    __tablename__ = 'shop'
    
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=100), unique=True) 
        
class Stock(Base):
    __tablename__ = 'stock'
    
    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'))    
    
class Sale(Base):
    __tablename__ = 'sale'
    
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, unique=True)
    sale_date = sq.Column(sq.TIMESTAMP)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'))    
    count = sq.Column(sq.Integer)

def create_db(username, password, db_name):
    try:
        connection = psycopg2.connect(user=username, password=password)
        connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        with connection.cursor() as cursor:
            cursor.execute('CREATE DATABASE %s' % (db_name, ))
    finally:
        if connection:
            connection.close()
            return print('Database created')  

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)