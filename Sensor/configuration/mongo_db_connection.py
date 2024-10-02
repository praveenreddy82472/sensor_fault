import pymongo
from Sensor.constant.database import DATABASE_NAME
#from Sensor.constant.env_variable import MONGODB_URL_KEY
import certifi
import os
ca = certifi.where()

print(DATABASE_NAME)
class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:

            if MongoDBClient.client is None:
                mongo_db_url = 'mongodb+srv://tumatipraveenreddy23:Praveen987@cluster0.reoxs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
                print(mongo_db_url)
                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url) 
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e