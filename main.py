#Network Chuck Lists
supplies = ["tent", "sleeping bag", "water", "raspberry pi", "coffee", "knife", "kettle", "ethernet cable",
            "flash drive", "beard oil", "marshmallows", "chocolate bar", "graham crackers", "mugs",
            "cooler", "meat", "bread", "grill", "flashlight"]
camp_site = ["Trooper's Creek", 404, 89.3, True]

chuck_brings = int(input("What should Network Chuck bring? Enter the number.\n"))
me_brings = int(input("And what am I bringing? Enter the number.\n"))
print("Ok so out of all our items, Network Chuck will bring " + supplies[chuck_brings] + " and I will bring " + supplies[me_brings] + ".\n")

# Adding toilet paper and a portable bidet to the list supplies[] in three ways
# .append , .extend , adding / concatenating lists , and .insert
# supplies.append("toilet paper")
# supplies.extend(["toilet paper", "bidet"])
#supplies = supplies + ["toilet paper", "bidet"]
supplies.insert(0, "toilet paper")
supplies.insert(-1, "bidet")

print(supplies)
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
