# Coffee Shop 

## Overview

This project is a  **inheritance** and define various `Beverage` objects with their respective properties.

- Overriding inherited methods from the parent class in derived classes.
- Installing `pytest` and unit testing your code.

I've created a base `Beverage` class and specific classes for different types of beverages like `Coffee` and `FruitJuice`. Additionally, a `DrinkOrder` class will organize beverages and provide a summary of a drink order. 

## Project Files

This project consists of five files:

1. **Beverage.py**: Defines the general `Beverage` class.
2. **Coffee.py**: Defines the `Coffee` class, which inherits from `Beverage`.
3. **FruitJuice.py**: Defines the `FruitJuice` class, which inherits from `Beverage`.
4. **DrinkOrder.py**: Defines the `DrinkOrder` class for managing a customer’s drink order.
5. **testFile.py**: Contains unit tests for the `Beverage`, `Coffee`, `FruitJuice`, and `DrinkOrder` classes using `pytest`.

## Class Details

# Beverage Class

The `Beverage` class represents a general beverage with its size in ounces and price.

### Attributes:
- `ounces`: The size of the beverage in ounces.
- `price`: The price of the beverage.

### Methods:
- `__init__(self, ounces, price)`: Initializes the beverage with its size and price.
- `getInfo(self)`: Returns a string representing the beverage information.

### Example:
```python
b1 = Beverage(16, 20.5)
print(b1.getInfo())  # Output: "16 oz, $20.50"
```

---

# Coffee Class

The `Coffee` class represents a coffee beverage and extends the `Beverage` class.

### Attributes:
- Inherits `ounces` and `price` from `Beverage`.
- `style`: A string representing the coffee style (e.g., `"Espresso"`).

### Methods:
- `__init__(self, ounces, price, style)`: Initializes the coffee with its size, price, and style.
- `getInfo(self)`: Overrides the `getInfo()` method to include the coffee style in the returned string.

### Example:
```python
c1 = Coffee(8, 3.0, "Espresso")
print(c1.getInfo())  # Output: "Espresso Coffee, 8 oz, $3.00"
```

---

# FruitJuice Class

The `FruitJuice` class represents a fruit juice beverage and extends the `Beverage` class.

### Attributes:
- Inherits `ounces` and `price` from `Beverage`.
- `fruits`: A list of fruits used in the juice (e.g., `["Apple", "Guava"]`).

### Methods:
- `__init__(self, ounces, price, fruits)`: Initializes the juice with its size, price, and list of fruits.
- `getInfo(self)`: Overrides the `getInfo()` method to include the fruits used in the returned string.

### Example:
```python
juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
print(juice.getInfo())  # Output: "Apple/Guava Juice, 16 oz, $4.50"
```

---

# DrinkOrder Class

**File:** `DrinkOrder.py`

The `DrinkOrder` class manages a list of beverage objects (either `Coffee` or `FruitJuice`) and calculates the total price of the order.

### Attributes:
- `drinks`: A list to store beverage objects.

### Methods:
- `__init__(self)`: Initializes the order with an empty list of drinks.
- `addBeverage(self, beverage)`: Adds a beverage to the order.
- `getTotalOrder(self)`: Returns a formatted string listing all the beverages in the order and the total price.

### Example:
```python
c1 = Coffee(8, 3.0, "Espresso")
juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
order = DrinkOrder()
order.addBeverage(c1)
order.addBeverage(juice)
print(order.getTotalOrder())
# Output:
# Order Items:
# * Espresso Coffee, 8 oz, $3.00
# * Apple/Guava Juice, 16 oz, $4.50
# Total Price: $7.50
```

---

# Conclusion

This project demonstrates the use of object-oriented programming principles to model a simple beverage ordering system. By defining classes for different types of beverages, such as `Beverage`, `Coffee`, and `FruitJuice`, we can encapsulate the attributes and behaviors associated with each beverage type. The `DrinkOrder` class allows users to manage multiple beverages, providing functionality to add items and calculate the total price of the order.

Through this implementation, we highlight the advantages of code reusability, maintainability, and organization that come with OOP. The project serves as a foundational example for anyone looking to understand how to build more complex systems with Python. Future improvements could include adding additional beverage types, implementing user input for dynamic ordering, and enhancing the user interface.

Thank you for exploring this project!

