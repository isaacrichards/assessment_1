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
                                                   #the numbers in 'grouped' are not used, just the index of the DataFrame for the group names. 
                     
        group_data_list = []

        for group in grouped.index:
        
            grouped_data = self.data[self.data["group"] == group]#extract only data corresponding to the group from the whole database (stored in the attribute self.data)
    
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

    def train(self):

        
        #storing and altering the data into appropriate units (km --> m & days --> s)
        training_x_variable = (self.data[["distance_km"]]*1000)**3
        training_y_variable = (self.data["period_days"]*86400)**2


        from sklearn import linear_model

        #create an instance of the model
        model = linear_model.LinearRegression(fit_intercept=True)

        #import train_test_split
        from sklearn.model_selection import train_test_split

        x_train, x_test, y_train, y_test = train_test_split(training_x_variable, training_y_variable, test_size=0.3, random_state=42)

        #fit the model to the training data defined above
        model.fit(x_train, y_train)

        # use the model to predict y-values of the testing set
        pred = model.predict(x_test)

        from sklearn.metrics import r2_score, mean_squared_error

        #validate the accuracy of the model
        print(f"model r2_score: {r2_score(y_test,pred)}")
        print(f"root mean squared error: {mean_squared_error(y_test,pred, squared=False)}")

        #calculate the mass of Jupiter following the procedure outlined before
        import numpy as np

        G = 6.67e-11
        
        mass_estimate = (4*np.pi**2) / (model.coef_[0]*G)

        #return this mass estimate

        print("The model predicts a mass of:", mass_estimate ,"kg")

