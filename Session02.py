# enteredName = input("Hello, I am Cobra. What is your name? ")
# enteredAge = int(input("Please enter your age: "))
# age_plus_five_years = enteredAge + 5

# =================================================
# Question 4 in the second session's Python guide.
# print("Hello. I am a Python script that determines if a number is even or odd.\n")
# entered_number = int(input("Please type in a whole number: "))

# if entered_number % 2 == 0:
#    print("The number " + str(entered_number) + " is an even number. Thanks and goodbye. ")
# else:
#    print("The number " + str(entered_number) + " is an odd number. Thanks and goodbye. ")

# ======================================================
# Question 5 - determine if the entered number is positive, negative, or zero.
# Print a message to the user and store the entered number.
# print("Hello. I am a Python script that determines if a number is positive, negative, or zero.\n")
# entered_number = int(input("Please type in a whole number: "))

# Determine if the number is positive, negative, or zero
# if entered_number == 0:
#    print("You entered " + str(entered_number) + " which is ZERO! :D ")
# elif entered_number < 0:
#     print("You entered " + str(entered_number) + " which is a negative number. :P ")
# else:
#     print("You entered " + str(entered_number) + " which is a positive number. :) ")

# ======================================
# Question 6 - ask user for fave fruit.
# Print a welcome and instructions. Get the entered fruit.
print("Hello. I am a Python script to add fruits to a list.\n")
entered_fruit = input("Please type in the name of your favorite fruit: ")

# Create a list to store entered fruits.
favorite_fruits = []

# insert the entered fruit into the list
favorite_fruits.append(entered_fruit)

# Print the list so far
print("Thanks. So far you have the following in your list: ", favorite_fruits)

# Ask if the user would like to add another fruit to the list?
# Then determine if the user wants to continue or not and do appropriate steps
while True:
    keep_going = input("\nWould you like to add another fruit to your list? Yes or no: ")
    # Determine what was entered
    if keep_going == "Yes" or keep_going == "yes" or keep_going == "Y" or keep_going == "y":
        another_fruit = input("Please type in the name of another fruit to add to your list: ")
        favorite_fruits.append(another_fruit)
        print("You have added " + another_fruit + " to your list. So far you have the following in your list: ", favorite_fruits)
    else:
        break # exits the loop
# Print out the list and end the program
print("Thanks. You have the following in your list: ", favorite_fruits)
