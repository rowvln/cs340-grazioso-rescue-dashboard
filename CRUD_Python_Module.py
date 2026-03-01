# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelterCRUD: 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        #  
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if not data:
            return False
        try:
            result = self.collection.insert_one(data)
            return result.acknowledged
        except Exception:
            return False

    # Create method to implement the R in CRUD.
    def read(self, query, projection=None):
        if query is None:
            return []
        try:
            cursor = self.collection.find(query, projection) if projection else self.collection.find(query)
            return list(cursor)
        except Exception:
            return []