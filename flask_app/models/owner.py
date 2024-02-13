from flask_app.config.mysqlconnection import connectToMySQL
from .pet import Pet

class Owner: #instance of the class = object
        def __init__( self , data ):
                self.id = data['id']
                self.name = data['name']
                self.created_at = data['created_at']
                self.updated_at = data['updated_at']
                self.pets = []

        @classmethod
        def get_all(cls):
                query = "SELECT * FROM owners;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
                results = connectToMySQL('pets_and_owners_schema').query_db(query)
        # Create an empty list to append our instances of owners
                owners = []
        # Iterate over the db results and create instances of owners with cls.
                for owner in results:
                        owners.append( cls(owner) )
                return owners

# gets all the owners and returns them in a list of user objects
# class method to save our owners to the database
        @classmethod
        def save(cls, data ):
                query = "INSERT INTO owners (name) VALUES (%(name)s);"
                return connectToMySQL('pets_and_owners_schema').query_db(query,data)

        @classmethod
        def get_one_pets(cls,data):
                query = "SELECT * FROM owners LEFT JOIN pets on owners.id = pets.owner_id WHERE owners.id = %(id)s;"
                results = connectToMySQL('pets_and_owners_schema').query_db(query,data)
                current_owner = cls(results[0])
                # print(results)
                # print(current owner.id)
                for field in results:
                        member = {
                                'id':field['pets.id'],
                                'first_name': field['first_name'],
                                'last_name': field['last_name'],
                                'age': field['age'],
                                'owner_id': field['owner_id'],
                                'created_at': field['pets.created_at'],
                                'updated_at': field['pets.updated_at']
                        }
                        current_owner.pets.append(Pet(member))
                return current_owner