import numpy as np

class DataBase:
    
    def __init__(self,route):
        self.DB = np.loadtxt("./" + route, dtype = str)
    
    @property
    def bookname(self):
        return self.DB[:,0]
    @property
    def author(self):
        return self.DB[:,1]
    @property
    def publicationyear(self):
        return self.DB[:,2]
    @property
    def publisher(self):
        return self.DB[:,3]
    @property
    def genre(self):
        return self.DB[:,4]
