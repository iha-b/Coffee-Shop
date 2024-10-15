from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice

class DrinkOrder(Beverage):
    def __init__(self):
        self.drinks = []
    def addBeverage(self, beverage):
        self.drinks.append(beverage)
    def getTotalOrder(self):
        if not self.drinks:
            return "Order Items:\nTotal Price: $0.00"
        total_price = 0
        order = []
        for i in self.drinks:
            order.append("* " + i.getInfo())
            total_price += i.getPrice()
        
        s = "Order Items:"
        s+= "\n" + "\n".join(order)
        s+= "\nTotal Price: ${:.2f}".format(total_price)
        return s

