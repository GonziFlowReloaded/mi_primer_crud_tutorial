from pymongo import MongoClient
from core.settings import settings

class MongoDB:
    def __init__(self, dbname="tareas", uri=settings.MONGO_URI, default_collection=settings.MONGO_DEFAULT_COLLECTION):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]
        self.default_collection = default_collection

    def insert_one(self, collection, document):
        return self.db[collection].insert_one(document)

    def find_one(self, collection, query):
        return self.db[collection].find_one(query)

    def update_one(self, collection, query, update):
        return self.db[collection].update_one(query, update)

    def delete_one(self, collection, query):
        return self.db[collection].delete_one(query)
    
    def find_all(self, collection):
        return list(self.db[collection].find())
    
    
mongo_db = MongoDB()