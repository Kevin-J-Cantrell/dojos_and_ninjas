from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojos


class Ninja:
    mydb = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
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
    def create(cls, data):
        query = "INSERT INTO ninjas ( first_name , last_name , age , dojo_id) VALUES ( %(first_name)s , %(last_name)s , %(age)s ,%(dojo_id)s);"
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL(cls.mydb).query_db(query, data)
        print(result)
        return result

    @classmethod
    def delete(cls, data):
        print('delete')
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        connectToMySQL(cls.mydb).query_db(query, data)

    @classmethod
    def update(cls,data):
        query = """
        UPDATE ninjas 
        SET first_name = %(first_name)s , last_name = %(last_name)s , age = %(age)s
        WHERE id = %(id)s
        """
        result = connectToMySQL(cls.mydb).query_db(query, data)
        print(result)
        return result
    
    @classmethod     # necessary for one getting one item or data from db
    def get_one(cls,data):
        query = """
        SELECT * FROM ninjas 
        WHERE id = %(id)s
        """     
        result = connectToMySQL(cls.mydb).query_db(query, data)
        print(result)
        get_one = cls( result[0] )

        return get_one