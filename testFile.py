from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder

def test_Beverage():
    b2 = Beverage(12, 10)
    output2 = b2.getInfo()
    b3 = Beverage(11, 30.39)
    output3 = b3.getInfo()
    b4 = Beverage(9, 9.9)
    output4 = b4.getInfo()
    assert output2 == "12 oz, $10.00"
    assert output3 == "11 oz, $30.39"
    assert output4 == "9 oz, $9.90"
def test_Coffee():
    c2 = Coffee(9, 2.5, "Americano")
    output2 = c2.getInfo()
    c3 = Coffee(12, 4, "Mocha")
    output3 = c3.getInfo()
    c4 = Coffee(10, 5.55, "Cappuccino")
    output4 = c4.getInfo()
    assert output2 == "Americano Coffee, 9 oz, $2.50"
    assert output3 == "Mocha Coffee, 12 oz, $4.00"
    assert output4 == "Cappuccino Coffee, 10 oz, $5.55"
def test_FruitJuice():
    j2 = FruitJuice(14, 5, ["Strawberry", "Orange"])
    output2 = j2.getInfo()
    j3 = FruitJuice(12, 4.75, ["Watermelon", "Pomegranate"])
    output3 = j3.getInfo()
    j4 = FruitJuice(9, 5.3, ["Cranberry"])
    output4 = j4.getInfo()
    assert output2 == "Strawberry/Orange Juice, 14 oz, $5.00"
    assert output3 == "Watermelon/Pomegranate Juice, 12 oz, $4.75"
    assert output4 == "Cranberry Juice, 9 oz, $5.30"
def test_DrinkOrder():
    c2 = Coffee(9, 2.5, "Americano")
    j2 = FruitJuice(14, 5, ["Strawberry", "Orange"])
    order2 = DrinkOrder()
    order2.addBeverage(c2)
    order2.addBeverage(j2)
    output2 = order2.getTotalOrder()
    assert output2 == ("Order Items:\n* Americano Coffee, 9 oz, $2.50\n* Strawberry/Orange Juice, 14 oz, $5.00\nTotal Price: $7.50")
    order3 = DrinkOrder()
    output3 = order3.getTotalOrder()
    assert output3 == "Order Items:\nTotal Price: $0.00"
