# Colter Makowski
# UWYO COSC 1010
# Submission Date 11/18/24
# Lab 09
# Lab Section:15
# Sources, people worked with, help given to:
# Your
# Comments
# Here

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria

# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.
class Pizza:
    def __init__(self, size, sauce = "Red"):
        self.size = size
        self.sauce = sauce if sauce else "red"
        else:
            self.sauce = sauce
        self.Toppings = ["cheese"]
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
    def set_size(size):
        if int(size).isdigit() and int(size) > 10:
            slef.size = int(size)
        else:
            self.size = 10
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
    def set_toppings(self, toppings):
        self.Toppings.append(toppings)
    def getSize(self):
        return self.size
    def get_sauce(self):
        return self.sauce
    def getAmountOfToppings(self):
        return self.Toppings
# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
class Pizzeria():
    def __init__(self):
        self.orders = 0
        self.price_per_inch = 0.3
        self.price_per_topping=0.6
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
    def placeOrder(self):
        self.orders += 1
        print("Please enter the size of pizza, as a whole number. The smallest size is 10")
        self.size = input("")
        # Get the sauce, and toppings
        print("What kind of sauce would you like?")
        print("Leave blank for red sauce")
        self.sauce = input("")
        print("Please enter the toppings you would like, leave blank when done")
        Toppings = []
        while True:
            topping = input()
            if (topping ==""):
                break
            else:
                Toppings.append(topping)
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
    def getPrice(self):
        amount = (pizza.getSize() * price_per_inch) + len(Toppings) * price_per_topping
        return amount
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
    def getReceipt(self):
        return f"You ordered a {Pizza.size} inch pizza with garlic sauce and the following toppings:"
        for i in (0, len(Toppings)):
            print(Toppings[i])
        #1 price for the size: You ordered a 20" pizza for 12.0
        print(f"You ordered a {size}inch pizza for {pizza.getSize()* price_per_inch} ")
        #2 price for the toppings: You had 3 topping(s) for $0.8999999999999999
        print(f"You had {len(Toppings)} topping(s) for {len(Toppings) * price_per_topping}")
        #3 total price(call self.getPrice()) below: Your total price is $12.9
        receipt += f"Your total price is ${self.getPrice()}"
        print(receipt)
# - getNumberOfOrders()
#   - This will simply return the number of orders.
    def getNumberOfOrders(self):
        return self.orders
# - Declare your pizzeria object.
myPizzeria = Pizzeria()
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
while True:
    # Ask the user if they wanna place an order or exit
    print("Would you like to place an order? exit to exit")
    order_pizza = input("")
    if order_pizza.lower() == 'exit':
        break
# - Call the placeOrder() method with your class instance.
    myPizzeria.placeOrder()
# - After the order is placed, call the getReceipt() method.
    myPizzeria.getReceipt()
    print("Would you like to place an order? exit to exit")
    continue
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.

myPizzeria.getNumberOfOrders()
# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""