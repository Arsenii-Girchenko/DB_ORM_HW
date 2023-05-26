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
        # if data["model"] == "publisher":
        #     new_line = Publisher(id=data["pk"], name=data["fields"]["name"])
        # if data["model"] == "book":
        #     new_line = Book(id=data["pk"], title=data["fields"]["title"], id_publisher=data["fields"]["id_publisher"])
        # if data["model"] == "shop":
        #     new_line = Shop(id=data["pk"], name=data["fields"]["name"])
        # if data["model"] == "stock":
        #     new_line = Stock(id=data["pk"], id_shop=data["fields"]["id_shop"], id_book=data["fields"]["id_book"], count=data["fields"]["count"])
        # if data["model"] == "sale":
        #     new_line = Sale(id=data["pk"], price=data["fields"]["price"], date_sale=data["fields"]["date_sale"], count=data["fields"]["count"], id_stock=data["fields"]["id_stock"])
        # session_name.add(new_line)
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[data.get('model')]
        session_name.add(model(id=data.get('pk'), **data.get('fields')))
    return session_name.commit()

