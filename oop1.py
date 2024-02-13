class Fruits:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"I bought {self.name} worth {self.price}kes each")


myfruit = Fruits("bananas", 20)
myfruit.show()
myfruit2 = Fruits("apples", 30)
myfruit2.show()
myfruit3 = Fruits("mangoes", 20)
myfruit3.show()
myfruit4 = Fruits("guavas", 10)
myfruit4.show()
myfruit5 = Fruits("pawpaws", 120)
myfruit5.show()
