from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):

    #initialize the MongoClient in AAC database animal collection

    def __init__(self):
        USER = 'aacuser'
        PASS = 'pierogi'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32549
        DB = 'AAC'
        COL = 'animals'

    #initialize the connection

        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    #CRUD - create new database entry with print statement confirmation

    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)
            print("true")
        else:
            raise Exception("Nothing to save, data parameter is empty")
            print("false")

    #CRUD - read database and return entries that match query

    def read(self, data):
        if data is not None:
            results = self.database.animals.find(data)
            for entry in results:
                print(entry)
        else:
            return []

    #CRUD - update database and return the number of objects modified in the collection

    def update(self, query, new_values):
        if new_values is not None:
            updated_entries = self.database.animals.update_many(query, new_values)
            print(updated_entries.modified_count, " document(s) updated.")
        else:
            return []

    #CRUD - delete document within database and return the number of objects removed from the collection

    def delete(self, data):
        if data is not None:
            deleted_entries = self.database.animals.delete_one(data)
            print(deleted_entries.deleted_count, " document deleted.")
        else:
            return []
            

if __name__ ==  "__main__":
    
    #test for CRUD functionality

    operation = AnimalShelter()

    #testing create 

    print("Running create function ...")
    add_dict = {'rec_num': 10001, 'age_upon_outcome': '3 years', 'animal_id': 'A999999', 'animal_type': 'Cat', 'breed': 'Domestic Short hair tortie', 'color': 'Peach/gray', 'date_of_birth': '2020-08-13 13:13:00', 'monthyear': '2020-08-15T12:13:00', 'name': '*Pierogi', 'outcome_subtype': '', 'outcome_type': 'Adoption', 'sex_upon_outcome': 'Spayed Female', 'location_lat': 30.3020557753236, 'location_long': -97.3259884527128, 'age_upon_outcome_in_weeks': 12.4}
    operation.create(add_dict)

    #testing read on data created

    print("Running read function ...")
    query = {"breed" : "Domestic Short hair tortie"}
    operation.read(query)

    #testing update functionality

    print("Running update function ...")
    new_values = {"$set" : {"name":"*George"}}
    operation.update(query, new_values)
    operation.read(query)

    #testing delete functionality

    print("Running delete function ...")
    operation.delete(query)
    







    


