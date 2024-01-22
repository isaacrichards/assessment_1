import pandas as pd

class Moons:

    def __init__(self):

        self.data = self.data()#attribute the whole data base to Moons.data
        self.names = self.names()#list of moon names
        self.grouped_data = self.grouped_data()
        
    def data(self):
        """Open and read the Jupiter moons database, and save it as an attribute of this class .data"""

        database_service = "sqlite"

        database = "data/jupiter.db"

        connectable = f"{database_service}:///{database}"

        query = "SELECT * FROM moons"#query to retrieve all of the data on the moons table

        selected_data = pd.read_sql(query, connectable)#use sql service to open database   
        
        selected_data.set_index("moon", inplace = True)#inplace kwarg keeps index change constant

        return selected_data
    

    def grouped_data(self):

        grouped = self.data.groupby("group").mean()#group the data by finding average values for each of the variables for each of the groups.
                                                   #the numbers in grouped are not used, just the index of the DataFrame. 
                     
        group_data_list = []

        for group in grouped.index:
        
            grouped_data = self.data[self.data["group"] == group]
    
            group_data_list.append(grouped_data)

        return group_data_list



    def names(self):
        """Determine the names for each of the moons, useful when data from one moon is required but the name is unkown, save a .names attribute of the 'moons' class"""
        
        
        name_list = []
        
        for name in self.data.index:#iterate over each item in the .data index (the moon names) and store them in a list
            
            name_list.append(name)
        
        return name_list
    

    def plot(self, x_value, y_value):

        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()

        plt.scatter(self.data[x_value], self.data[y_value])
        plt.xlabel(x_value)
        plt.ylabel(y_value)
        
        plt.show()
       

