from flask_app.models.ninja import Ninja
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo():

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def create_dojo(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"

        result = connectToMySQL('ninja_dojo').query_db(query, data)

        return result
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('ninja_dojo').query_db(query)

        dojos = []

        for item in results:
            dojos.append(Dojo(item))

        return dojos

    @classmethod
    def add_ninja_to_dojo(cls,data):
        query = "INSERT INTO ninjas (dojos_id, first_name, last_name, age) VALUES (%(dojos_id)s, %(first_name)s, %(last_name)s, %(age)s)"
        
        results = connectToMySQL('ninja_dojo').query_db(query,data)

        return results

    @classmethod
    def get_ninjas_by_dojo(cls,data):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s"

        results = connectToMySQL('ninja_dojo').query_db(query,data)

        #print(results)

        dojo = []
        
        for item in results:
            ninja_data = {
                'id': item['id'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'age': item['age'],
                'created_at': item['created_at'],
                'updated_at': item['updated_at'],
                'dojos_id': item['dojos_id'],
            }
            dojo.append(ninja_data)

        return dojo