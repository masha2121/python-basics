class Car:

    def __init__(self, make, model, year,color):
        self.color = color
        self.make = make
        self.model = model
        self.year = year


    def onyesha(self):
        print(f"my dream car is a{self.color} {self.make} and my model is "
              f"{self.model} manufactured in {self.year}")


myobj = Car("black")
myobj.onyesha()
myobj2 = Car("volkswagen", "golf", 2007)
myobj2.onyesha()
