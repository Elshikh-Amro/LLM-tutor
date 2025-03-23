class car :
    def __init__(self,brand, color):
     self.brand = brand
     self.color = color
        
    def describe(self):
        return f"this car is {self.color} {self.brand}"

car1 = car("BMW", "red")
print(car1.describe())