class Gari:    def __init__(self,make ,model ,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading =0
    def describe_gari(self):
        return f"{self.model} {self.year} {self.make}"
    def read_odometer(self):
        return f"this car has {self.odometer_reading} milage"
    def update_odometer(self,milage):
        if milage >= self.odometer_reading:
            self.odometer_reading= milage
        else:
             print("you cant roll back an odometer")
    def increament_odometer(self,miles):
        self.odometer_reading+=miles
my_car=Gari("Toyota", "vitz",2001)
print(my_car.describe_gari())
print(my_car.read_odometer())
my_car.update_odometer(100)
print(my_car.read_odometer())
my_car.increament_odometer(60)
print(my_car.read_odometer())