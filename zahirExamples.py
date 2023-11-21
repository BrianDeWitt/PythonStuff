# This is a sample Python script.

# Greet the team
print("Hello everyone!")

# Grab someone's name and store it in a variable called "enteredName"
enteredName = input("What is your name? ")

# Print a greeting using the entered name. Print a special greeting for a specific name.
if enteredName == "Python" or enteredName == "python":
    print("Whoa! As in _THE_ " + enteredName + "?!?!?!?!? It is an honor.")
else:
    print("Nice to meet you, " + enteredName + ". :D ")

# Variables for calculating the area of a circle
radius = float(input("Please type in a radius. It must be a number. "))
pi_constant = 3.14159
area = pi_constant * radius ** 2
print("The area of the circle with radius " + str(radius) + " is " + (str(area)))

# Boolean example
is_raining_input = input("Is it raining right now? Yes or no? ")
has_umbrella_input = input("Did you bring an umbrella? Yes or no? ")
likes_rain_input = input("Do you like walking in the rain? Yes or no? ")

# Convert user input to a boolean value. Also be case agnostic.
is_raining = is_raining_input.lower() in ["yes", "y"]
has_umbrella = has_umbrella_input.lower() in ["yes", "y"]
likes_rain = likes_rain_input.lower in ["yes", "y"]

can_go_out = not is_raining or has_umbrella or likes_rain

if can_go_out:
    print("You decided to go out for a walk. ")
else:
    print("You decided to stay inside for a bit. ")

# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
