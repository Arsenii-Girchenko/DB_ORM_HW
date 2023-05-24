import os
import json
from pprint import pprint
from DB_Classes import Publisher, Book, Shop, Stock, Sale

def fill_in_db(session_name, folder_name):
    for filename in os.scandir(os.path.join(os.getcwd(), folder_name)):
        if filename.name == 'test_data.json':
            with open (filename, 'r', encoding='utf-8') as f:
                test_data_list = json.load(f) 
    for data in test_data_list:
        # if data["model"].title() == "Publisher":
        #     Publisher(name=data["fields"]["name"])
        # elif data["model"].title() == "Book":
        #     Book(title=data["fielda"]["title"], id_publisher=data["fielda"]["id_publisher"])
        # elif data["model"].title() == "Shop":
        #     Shop(name=data["fields"]["name"])
        # elif data["model"].title() == "Stock":
        #     Stock(id_shop=data["fielda"]["id_shop"], id_book=data["fielda"]["id_book"], count=data["fielda"]["count"])
        # elif data["model"].title() == "Sale":
        #     Sale(price=data["fielda"]["price"], sale_date=data["fielda"]["date_sale"], count=data["fielda"]["count"], id_stock=data["fielda"]["id_stock"])
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[data.get('model')]
        session_name.add(model(id=data.get('pk'), **data.get('fields')))          
    return session_name.commit()

