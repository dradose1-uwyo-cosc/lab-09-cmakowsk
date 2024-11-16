# Colter Makowski
# UWYO COSC 1010
# Submission Date 11/18/24
# Lab 09
# Lab Section:15
# Sources, people worked with, help given to: chat GPT to fix and finallize small errors
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
        self.size = int(size) if size.isdigit() and int(size) > 10 else 10
        self.sauce = sauce if sauce.strip() else "Red"
        self.toppings = ["cheese"]
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
    def add_toppings_to_list(self, *toppings):
        self.toppings.extend(toppings)
    def getSize(self):
        return self.size
    def get_sauce(self):
        return self.sauce
    def get_toppings(self):
        return self.toppings
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
    price_per_inch = 0.6
    price_per_topping=0.3
    def __init__(self):
        self.orders = 0
        self.pizzas = []
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
        self.size = input("").strip()
        # Get the sauce, and toppings
        print("What kind of sauce would you like?")
        print("Leave blank for red sauce")
        self.sauce = input("").strip()
        print("Please enter the toppings you would like (one at a time), enter blank when done")
        toppings = []
        while True:
            topping = input("").strip()
            if not topping:
                break
            toppings.append(topping)
        pizza = Pizza(self.size, self.sauce)
        pizza.add_toppings_to_list(*toppings)
        self.pizzas.append(pizza)

# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
    def getPrice(self, pizza):
        size_cost = pizza.getSize() * Pizzeria.price_per_inch
        toppings_cost = len(pizza.get_toppings()) * Pizzeria.price_per_topping
        return size_cost + toppings_cost
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
    def getReceipt(self, pizza):
        size_cost = pizza.getSize() * Pizzeria.price_per_inch
        toppings_cost = len(pizza.get_toppings()) * Pizzeria.price_per_topping
        total_cost = self.getPrice(pizza)
        print(f"You ordered a {pizza.getSize()} inch pizza with {pizza.get_sauce()} sauce and the following toppings:")
        print(", ".join(pizza.get_toppings()))
        #1 price for the size: You ordered a 20" pizza for 12.0
        print(f"You ordered a {pizza.getSize()} inch pizza for ${size_cost}")
        #2 price for the toppings: You had 3 topping(s) for $0.8999999999999999
        print(f"You had {len(pizza.get_toppings())} topping(s) for ${toppings_cost}")
        #3 total price(call self.getPrice()) below: Your total price is $12.9
        print (f"Your total price is ${total_cost}")
        print("")
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
    myPizzeria.getReceipt(myPizzeria.pizzas[-1])
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.

print(f"{myPizzeria.getNumberOfOrders()} amount of orders were placed")
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