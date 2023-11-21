# This is a sample Python script.

# ======================================================================
# Network Chuck Episode 04

#Variable declarations
menu = "Espresso, flat white, long black, filter, cappuccino, frappuccino, macciato, hot chocolate, and chai.\n"

# Program
# Welcome the customer and get their name.
print("Hello, welcome to Network Chuck dot coffee!!! ")
name = input("What is your name? ")

if name == "Ben" and "Patricia":
    evil_status = input("Are you evil? ")
    if evil_status == "Yes":
        print("You're not welcome here Evil Ben! Get out!!")
        exit()
    else:
        print("Oh, so you're one of those good Bens? Come on in!")

print("Hello, " + name + ", thank you so much for coming in. Today we have the following items available: \n" + menu)
customerOrder = input("What would you like? ")
#orderTotal = price * float(customerOrderQuantity)

# Determine price of the ordered item
if customerOrder == "frappuccino":
    price = 13.00
elif customerOrder == "frap":
    price = 13.00
elif customerOrder == "Frappuccino":
    price = 13.00
elif customerOrder == "black coffee":
    price = 3.50
elif customerOrder == "Black coffee":
    price = 3.50
elif customerOrder == "Black Coffee":
    price = 3.50
elif customerOrder == "Cappuccino":
    price = 6.50
elif customerOrder == "cappuccino":
    price = 6.50
elif customerOrder == "Espresso":
    price = 4.50
elif customerOrder == "espresso":
    price = 4.50
elif customerOrder == "flat white":
    price = 5.50
elif customerOrder == "Flat white":
    price = 5.50
elif customerOrder == "Flat White":
    price = 5.50
elif customerOrder == "latte":
    whipOption = input("Would you like whipped cream? ")
    if whipOption == "Yes":
        price = 11.00
    else:
        price = 8.50
elif customerOrder == "Latte":
    whipOption = input("Would you like whipped cream? ")
    if whipOption == "Yes":
        price = 11.00
    else:
        price = 8.50
elif customerOrder == "filter":
    price = 5.00
elif customerOrder == "drip":
    price = 4.00
elif customerOrder == "Filter":
    price = 5.00
else:
    print("Sorry, we don't have that here.")

customerOrderQuantity = input("How many would you like? ")

print(price)
# ======================================================================
# Network Chuck Episode 03
#name = "NetworkChuck"
#age = 31
#actual_age = 31.96
#maths = 5 ** 7 + 6 / 9 * 6 - 4
#results = age + actual_age + maths
#print(results)

# ======================================================================
#Let's start a coffee shop together! We're going to build a coffee shop
# using some new Python programming concepts.
# Let's build robot Barista!

#menu = "Espresso, flat white, long black, filter, cappucino, macciato, hot chocolate, and chai.\nEach item costs $8.50\n"
#price = 8.50
#print("Hello! Welcome to Network Chuck Coffee!!!!!")
#name = input("What is your name? ")
##print("Hello, " + name + ", thank you so much for coming in. Today we have the following items available: \n" + menu)
#customerOrder = input("What would you like? ")
#customerOrderQuantity = input("How many would you like? ")
#orderTotal = price * float(customerOrderQuantity)
#print("Great choice, " + name + "! Your " + str(customerOrderQuantity) + " " + customerOrder + " will be ready soon. The total comes to $" + str(orderTotal) +", please.\n")


# =====================================================================================
# Network Chuck Episode 01
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# print("***All on one command line.***")
# print("Hello World!!!!! \nI am Iron Man \nNo, I am Tony Stark \nNo, I am Poppy.\n")

# print("\n***triple quotes***")
# print("""I am Iron Man.
#No, I am Tony Stark.
#No, I am Poppy.""")

#print("\n***Concating multiple strings***")
#print("I am Iron Man.\n" + "No, I am Tony Stark.\n" + "No, I am Poppy.\n")

#print("I am Poppy. \n" * 100)
# We are practicing Python... IT'S AWESOME!!!
# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
