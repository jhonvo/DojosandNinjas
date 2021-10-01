from dojoninja_app.config.mysqlconnection import connectToMySQL
from dojoninja_app.models import ninjas


class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []

    @classmethod
    def get_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("mydb").query_db(query)
        # print(results)
        dojos = []
        for line in results:
            dojos.append(Dojo(line))
            # print (line['id'])
        return dojos

    @classmethod
    def new_dojo(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        results = connectToMySQL("mydb").query_db(query, data)
        return results

    @classmethod
    def ninjasAtDojo(cls,num):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        data = {
            'id' : num
        }
        results = connectToMySQL("mydb").query_db(query,data)
        dojo = Dojo(results[0])
        for ninja_row in results:
            ninja_data = {
                'id' : ninja_row['ninjas.id'],
                'first_name' : ninja_row['first_name'],
                'last_name' : ninja_row['last_name'],
                'age' : ninja_row['age']
            }
            dojo.ninjas.append(ninjas.Ninja(ninja_data))
        print (dojo.ninjas)
        return dojo
    