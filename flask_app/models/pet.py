from flask_app.config.mysqlconnection import connectToMySQL

class Pet:
        def __init__( self , data ):
                self.id = data['id']
                self.first_name = data['first_name']
                self.last_name = data['last_name']
                self.age = data['age']
                self.owner_id = data['owner_id']
                self.created_at = data['created_at']
                self.updated_at = data['updated_at']

# gets all the users and returns them in a list of user objects
# class method to save our users to the database
        @classmethod
        def save(cls, data ):
                query = "INSERT INTO pets (first_name, last_name, age, owner_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(owner_id)s);"
                return connectToMySQL('owners_pets_schema').query_db(query,data)