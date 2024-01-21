import pandas as pd

class Moons:

    def __init__(self):

        self.data = self.data()#attribute the whole data base to Moons.data
        self.names = self.names()
        
        
    def data(self):
        """Open and read the Jupiter moons database, and save it as an attribute of this class .data"""

        database_service = "sqlite"

        database = "data/jupiter.db"

        connectable = f"{database_service}:///{database}"

        query = "SELECT * FROM moons"

        selected_data = pd.read_sql(query, connectable)   
        
        selected_data.set_index("moon", inplace = True)

        return selected_data
    
    
    def names(self):
        """Determine the names for each of the moons, useful when data from one moon is required but the name is unkown, save a .names     attribute of the 'moons' class"""
        
        
        name_list = []
        
        for name in self.data.index:
            
            name_list.append(name)
        
        return name_list
    
    def plot(self, x_value, y_value):

        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()

        plt.scatter(self.data[x_value], self.data[y_value])
        plt.xlabel(x_value)
        plt.ylabel(y_value)
        
        plt.show()
       

