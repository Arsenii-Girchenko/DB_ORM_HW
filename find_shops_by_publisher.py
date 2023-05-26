import os
import json
from pprint import pprint
from DB_Classes import Publisher, Book, Shop, Stock, Sale

def find_shop_by_publisher(user_input, session_name):        
    if user_input.isnumeric() == True:      
        shops_by_pub = session_name.query(Book.title, Shop.name, Sale.price, Sale.date_sale
            ).join(Stock, Stock.id_book == Book.id
                ).join(Shop, Shop.id == Stock.id_shop
                    ).join(Sale, Sale.id_stock == Stock.id
                        ).join(Publisher, Book.id_publisher == Publisher.id
                            ).filter(Publisher.id == user_input)           
    else:       
        shops_by_pub = session_name.query(Book.title, Shop.name, Sale.price, Sale.date_sale
        ).join(Stock, Stock.id_book == Book.id
            ).join(Shop, Shop.id == Stock.id_shop
                ).join(Sale, Sale.id_stock == Stock.id
                    ).join(Publisher, Book.id_publisher == Publisher.id
                        ).filter(Publisher.name == user_input)
    return shops_by_pub.all()