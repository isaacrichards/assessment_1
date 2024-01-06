import pandas as pd

class Moons:

    def __init__(self):

        self.data = self.data()#attribute the whole data base to Moons.data
        #self.names = self.names()


    def data(self):

        database_service = "sqlite"

        database = "data/jupiter.db"

        connectable = f"{database_service}:///{database}"

        query = "SELECT * FROM *"

        selected_data = pd.read_sql(query, connectable)            

        return selected_data

    #def names(self):      
    
