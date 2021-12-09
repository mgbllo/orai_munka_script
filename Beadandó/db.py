import queue_
from pymongo import MongoClient

DB_NAME = 'traffic'
HOST = 'localhost'
PORT = 27017
COLLECTION = 'data'


def create_db_connection():
    C_STRING = f'mongodb://{HOST}:{PORT}/{DB_NAME}'
    client = MongoClient(C_STRING)
    return client


client = create_db_connection()


def add_route_data(bus_id, data):
    client[DB_NAME][bus_id].insert_many(data)
    queue_.run_statistics_job()
    return 'data saved'


def get_all_data():
    return client[DB_NAME][COLLECTION].find()


def get_collections():
    filter = {"name": {"$regex": r"^(?!statistic)"}}
    return client[DB_NAME].list_collection_names(filter=filter)


def get_bus_data() -> dict:
    b = sorted(get_collections())
    data = dict()
    for i in b:
        data[i] = list(map(lambda x: x, client[DB_NAME][i].find()))
    return data


def init_database():
    client = create_db_connection()
    client.drop_database(DB_NAME)
