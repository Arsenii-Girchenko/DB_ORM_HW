import psycopg2
import sqlalchemy
import sqlalchemy as sq
from pprint import pprint
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from DB_Classes import create_db, create_tables, Publisher, Book, Shop, Stock, Sale
from fill_in_DB import fill_in_db
from find_shops_by_publisher import find_shop_by_publisher


if __name__ == '__main__':
    
    DBMS_name = 'postgresql'
    username = 'postgres'
    password = 'postgres'
    db_name = 'DB_bookshop_HW'
    folder_name = 'fixtures'
    
    create_db(username, password, db_name)
    
    DSN = "postgresql://postgres:postgres@localhost:5432/db_bookshop_hw"
    engine = sq.create_engine(DSN)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    fill_in_db(session, folder_name)
    
    user_input = input('enter ID or name of the publisher: ')
    pprint(find_shop_by_publisher(user_input, session))