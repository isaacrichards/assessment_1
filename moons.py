import pandas as pd

class Moons:

    def __init__(self):

        self.data = self.data()#attribute the whole data base to Moons.data
        self.names = self.names()
        
    def data(self):

        database_service = "sqlite"

        database = "data/jupiter.db"

        connectable = f"{database_service}:///{database}"

        query = "SELECT * FROM moons"

        selected_data = pd.read_sql(query, connectable)   
        
        selected_data.set_index("moon", inplace = True)

        return selected_data
    
    
    def names(self):
        
        name_list = []
        
        for name in self.data.index:
            
            name_list.append(name)
        
        return name_list

    #def names(self):

