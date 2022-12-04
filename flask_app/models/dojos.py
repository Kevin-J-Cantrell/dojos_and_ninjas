from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas
class Dojo:
    mydb = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data ['id']
        self.name = data ['name']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.ninjas = []
        
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        things = connectToMySQL(cls.mydb).query_db(query)
        print(things)
        # Create an empty list to append our instances of users
        output = []
        # Iterate over the db results and create instances of users with cls.
        for stuff in things:
            output.append( cls(stuff) )
        print(output)
        return output
    
    @classmethod
    def get_one_dojo(cls,data):
        query = """ 
        SELECT * FROM dojos
        LEFT JOIN ninjas 
        ON ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s;
                """
                        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.mydb).query_db(query,data)
        print(results)
        one_dojo = cls( results[0] )
        for row_from_db in results:
            
            if row_from_db["ninjas.id"] == None:
                continue
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "dojo_id" : row_from_db["dojo_id"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            
            one_dojo.ninjas.append(ninjas.Ninja( ninja_data ) )
        return one_dojo
    
    @classmethod
    def update_one_dojo(cls,data):
        query = """ 
            UPDATE dojos
            SET first_name = %(first_name)s, last_name = %(last_name)s , age = %(age)s
            WHERE id = %(id)s;
                """
                        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.mydb).query_db(query,data)
        print(results)
        one_dojo = cls( results[0] )

        return one_dojo
    
    @classmethod
    def create(cls, data ):
        print('created')
        query = "INSERT INTO dojos (name) VALUES ( %(name)s );"
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL(cls.mydb).query_db( query, data )
        return result
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        connectToMySQL(cls.mydb).query_db( query,data )