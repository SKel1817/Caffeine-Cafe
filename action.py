# Valerie Nielson
# CSI 1310
# Final Exam

# import sleep funtion
from time import sleep

# Create a Class that will do everything the for the order section
class Coffee_order:
    # set variables for the orders
    def __init__(self, drink, milk="Whole", size="small", extra="No"):
        self.drink = drink
        self.milk = milk
        self.size = size
        self.extra = extra

    # funtion that lists back order nicely
    def order(self):
        # list the order back to them, have them comfirm that it is correct
        print("You order your coffee")
        print("So just to repeat that back to you")
        # creates gap
        sleep(1)
        # lists it
        print(
            "You wanted a "
            + self.size
            + " "
            + self.drink
            + " with "
            + self.milk
            + " milk "
        )
        print("Special instructions: " + self.extra)
        # Creates gap
        print()
        # allows wait time between next funtion
        sleep(1)

    # funtion taht simulates waiting
    def wait(self):
        print("You wait for your order")
        # simiulates waiting
        for i in range(0, 5, 1):
            # prints this so user knows code is still running
            print("...")

    # funtion that allows tipping and reciveing
    def recieve(self):
        # receive drink
        print("Alright, Here is that " + self.drink + "enjoy!")
        print("*You See a Tip Jar*")
        # the tipping bit
        # Variable for if customer is tipping or not
        tip_choice = input("Would you like to tip?(y/n) ").lower().strip()
        # if statment for customer is tipping or not
        if tip_choice == "y":
            # Variable that collects tips
            tip = input("How much would you like to tip? ")
            print("Thank you so much!")
            # create gap
            print()
        else:
            # sets tip to 0 in case I use it later
            tip = "0"
            print("Thank you anyway!")
            # creates gap
            print()

    # Funtion that simulates consuming the drink
    def consume(self):
        # bunch of print statments
        print("You drink your drink")
        print("It has never tasted as good as this before")
        print("You feel so CAFFINATED")
        print("Back to the Main Menu we go")

    # Function that writes the order to a file
    def track(self):
        # open file as history
        with open("OrderHistory.txt", "a") as history:
            # lines that make turning them to strings easer
            # these are what is being printed
            si = self.size + "\n "
            dr = self.drink + "\n"
            mi = self.milk + " milk\n"
            ex = "Special Instructions: " + self.extra

            # appended those lines to the file, and convert to string
            history.write("\nThis customer ordered:\n")
            history.write(str(si))
            history.write(str(dr))
            history.write(str(mi))
            history.write(str(ex))
            history.write("\nEnd of customer\n")
