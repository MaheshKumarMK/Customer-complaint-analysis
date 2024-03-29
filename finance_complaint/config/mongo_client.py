import pymongo
import os
from finance_complaint.constant.environment.variable_key import MONGO_DB_URL_ENV_KEY
import certifi


ca = certifi.where()

class MongoDBClient:

    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:

            if MongoDBClient.client is None:

                mongo_db_url = MONGO_DB_URL_ENV_KEY #os.getenv(MONGODB_URL_KEY)

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