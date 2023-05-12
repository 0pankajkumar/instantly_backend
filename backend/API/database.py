import pymongo
import sys


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        try:
            self.client = pymongo.MongoClient("mongodb+srv://instantlykabaap:htFn7QMewQckHqhe@instantlycluster.x1lcgdx.mongodb.net/?retryWrites=true&w=majority") 
        except pymongo.errors.ConfigurationError:
            print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
            sys.exit(1)

        # use a database named "myDatabase"
        self.db = self.client.myDatabase

    def find(self, collection="users", query={"login_id": "805.bluebell@gmail.com"}):
      my_collection = self.db[collection]
      my_doc = my_collection.find_one(query)
      my_doc = [each for each in my_doc]
      print(my_doc)
      return my_doc



    def insert(self, collection="users", query={}):

        dummy_user_details = {
          "login_id": "805.bluebell@gmail.com",
          "password": "somepassword",
          "emails": ["pankaj@testube.in", "howdy@testube.in"],
          "campaigns": ["somehashedcampaignid", "anotherhashedcampignid"],
          "plan": "ultimatesamuraiplan",
          "credits_total_emails": 10,
          "credits_left_emails": 5
        }

        try: 
         result = my_collection.insert_one(query)

        # return a friendly error if the operation fails
        except pymongo.errors.OperationFailure:
          print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
          sys.exit(1)
        else:
          inserted_count = len(result.inserted_ids)
          print("I inserted %x documents." %(inserted_count))





























def connections():
    try:
      client = pymongo.MongoClient("mongodb+srv://instantlykabaap:htFn7QMewQckHqhe@instantlycluster.x1lcgdx.mongodb.net/?retryWrites=true&w=majority")
      
    # return a friendly error if a URI error is thrown 
    except pymongo.errors.ConfigurationError:
      print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
      sys.exit(1)

    # use a database named "myDatabase"
    db = client.myDatabase

    # use a collection named "recipes"
    my_collection = db["users"]

















# We can also find a single document. Let's find a document
# that has the string "potato" in the ingredients list.
# my_doc = my_collection.find_one({"login_id": "805.bluebell@gmail.com"})
# print(my_doc)

