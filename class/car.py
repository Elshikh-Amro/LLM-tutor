# Define a class named 'Car'
class Car:
    # The __init__ method is the constructor, which is automatically called when a new object is created.
    def __init__(self, brand, color):  
        # 'self' represents the instance of the class.
        # We store the 'brand' and 'color' attributes inside the instance using 'self'.
        self.brand = brand  # ✅ Assigns the brand value to the object's 'brand' attribute
        self.color = color  # ✅ Assigns the color value to the object's 'color' attribute  

    # This is a method that returns a description of the car.
    def describe(self):
        # ✅ Uses self.brand and self.color to access the object's attributes.
        return f"This car is a {self.color} {self.brand}."


car1 = Car("BMW", "red")
print(car1.describe())