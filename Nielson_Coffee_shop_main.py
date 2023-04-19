# Valerie Nielson
# CSI 1310
# Final Exam

# import statments!!!
from Nielson_action import Coffee_order as cof

# https://www.programiz.com/python-programming/time/sleep
from time import sleep

# these are all the lists and tuples
# this creates a varible for each of the ingridents for a drink
light = ["Brazil"]
medium = ["Costa Rica"]
dark = ["Organic Sumatra"]
cafe_au = ["Brazil", "Steamed Milk"]
latte = ["Espresso", "Steamed Milk"]
mocha = ["Espresso", "Chocolate", "Steamed Milk", "Whip Cream"]
carm = ["Espresso", "Carmel", "Steamed Milk", "Whip Cream"]
chai = ["Chai Mix", "Steamed Milk"]
hot = ["Chocolate", "Steamed Milk"]

# this connects the ingridents to the name of the proper drink
menu = {
    "Light Roast Coffee": light,
    "Medium Roast Coffee": medium,
    "Dark Roast Coffee": dark,
    "Cafe au Lait": cafe_au,
    "Cafe Latte": latte,
    "Mocha Latte": mocha,
    "Creamy Carmel Latte": carm,
    "Chai Tea Latte": chai,
    "Hot Chocolate": hot,
}

# this is just a list of all the coffees so its easier to do the ordering bit
bev = [
    "Light Roast Coffee",
    "Medium Roast Coffee",
    "Dark Roast Coffee",
    "Cafe au Lait",
    "Cafe Latte",
    "Mocha Latte",
    "Creamy Carmel Latte",
    "Chai Tea Latte",
    "Hot Chocolate",
]

# function that lists the menu nicely
def list_menu():
    for key, value in menu.items():
        print(str(key) + ": " + str(value))
        sleep(1)


def numbered_menu():
    # count that enters the number that the drink is
    count = 1
    # prints drink names
    for key, value in menu.items():
        print(str(count) + ". " + str(key))
        count += 1


# This begins the actual program and a very large and annoying if statment
# Greet the customer
print(
    "Welcome to Caffine Cafe where all your coffee dreams are lines of text on a screen"
)
print("What can we do for you today?")

# Creates infinte loop
while True:
    # Creates the Main Menu that allows for navigation
    print("Please enter the number of the option you would like to do!")
    print(
        "1. View the menu\n2. Order a Coffee\n3. Suggest a coffee\n4. Look at your customer history\n5. To leave the coffee shop"
    )
    # Variable that will allow user to move around
    cho_one = input("Enter the number you would like and then press enter: ")
    # if statment that will make each option happen

    # This if statment makes the menu display
    if cho_one == "1":
        print("\nWe have many items on our menu so here they are!")
        # Call funtion that lists the dictornary: menu
        list_menu()
        # create gap
        print()
        # Allows Main Menu screen to be delayed to allow for better formatiing
        sleep(3)

    # elif statment that allows the customer to order
    elif cho_one == "2":
        # Greet
        print("\nHi! What can I get for you?")
        # Call funtion that numbers the menu
        numbered_menu()
        # create gap
        print()
        # Make numbered variable that lets user choice drink
        drink_num = input(
            "Please select the number associated with you drink and then press enter: "
        )

        # try and execpt statment that allows the input to put into an interger and be subtracted
        try:
            drink_num = int(drink_num)
            drink = bev[drink_num - 1]
        # Execpt statment that stops entered letters from crashing the program
        except ValueError:
            print(
                "That is not a vaild drink option I am very disapointed in you, Back to the menu you go"
            )
            print("BONK!")
            print()
            sleep(3)
            continue
        # The second error that entering a letter causes
        except TypeError:
            continue
        # The thrid error the entering a letter causes, this makes it so the functions are hurt
        except NameError:
            continue
        # Asks user for size, uses string instead of integer,DOESN"T CHECK TO SEE IF USER ENTER PROPER THING
        size = (
            input(
                "Just enter the name of the size(Small, Medium, Large)\nWhat size would you like? "
            )
            .title()
            .strip()
        )
        # Asks user for milk type, uses string instead of integer,DOESN"T CHECK TO SEE IF USER ENTER PROPER THING
        milk = (
            input(
                "Just enter the name of the milk(Whole, Skim, Oat, or Soy)\n What milk would you like?"
            )
            .title()
            .strip()
        )
        # Asks user for extra, uses string instead of integer,DOESN"T CHECK TO SEE IF USER ENTER PROPER THING
        extra = (
            input("Anything else for you? (if yes, enter it in, if no enter no)")
            .title()
            .strip()
        )
        # puts order into the Class system in the action script
        cus_order = cof(drink, milk, size, extra)
        # Calls the function in the action script the lists order back
        cus_order.order()
        # Calls the function in the action script that tracks the customers history
        cus_order.track()
        # create gap
        print()
        # Calls the function in the action script that simulates waiting
        cus_order.wait()
        # Calls the funciton in teh action script that simulates recieveing the drink
        cus_order.recieve()
        # Calls the fucntion in the actions script that simulates consuming the drink
        cus_order.consume()
        # generates delay before printing the main menu
        sleep(3)
        print()

    # elif statment that allows user to suggest a coffee
    elif cho_one == "3":
        print("So you wanna suggest a coffee? Alrighty lay it one me")
        # gets name of coffee and adds it to the bev list
        suggestion = input("Type name of Coffee here").title()
        bev.append(suggestion)

        # gathers ingridents and puts it in an empty list so we can but it in the dictornary
        print("Thats a cool name but whats in it?")
        # create empty list
        sug = []

        # keeps adding to sug unless user enters N
        while True:
            # variable the gathers ingredents
            ingre = input("Enter the first ingrident here, enter N when done").title()
            # adds it the sug list
            sug.append(ingre)
            # prints it so the user knows what they have added, this will include 'N' the first time
            print(sug)
            # stops while loop
            if ingre == "N":
                # deletes the N out of the list
                sug.pop()
                # breaks the While loop
                break

        print("Thats a pretty sick drink I am adding that to the menu now!")
        # add to menu dictornary
        menu[suggestion] = sug
        # call funtion that lists menu dictornary
        list_menu()
        print("See its up there now! well done")
        # generates wait time before displaying main menu
        sleep(3)
        print()

    # elif statment that allows user to look at previous orders
    elif cho_one == "4":
        print("We have many happy customers! our history includes...")
        # Read data from a file for sure, file will have previous orders
        # open file, as a varaible
        with open("OrderHistory.txt") as customer:
            # read the file
            his = customer.read()
        # print the file
        print(his)
        # Create gap
        print()
        # generate wait time for main menu
        sleep(3)
    # elif statment that ends the while loop and allows user to leave
    elif cho_one == "5":
        print("You wanna leave? well alright, have a great day!")
        # create gap
        print()
        break
    # else statment that catchs all letters, invaild numbers and special characters so it doesn't error out
    else:
        print("PLEASE ENTER A VAILD NUMBER!!!")
        print()
