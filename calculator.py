import definitions
# The line above will let you separate your concerns by defining functions your calculator might use in a separate file.

# print("Welcome to the Python Calculator\n\nWhat would you like to do?")
# budget = input("What is your total budget?")
# spent = input("How much money have you spent?")

def often_spent(time):
    if time == "weekly":
        print("How many times in a week do you purchase this item?")
        times_per_week = input()
        times_per_week = float(times_per_week)
        cost_per_week = times_per_week * cost
        print ("This is how much you spend on " + item + " every week: " + str(cost_per_week)) + "dollars"
print("Welcome to Spending Calculator!), We help you calculate your spending to help you budget better!")
item = input ("What is the item that you would like us to calculate the spending of?")
cost = input("How much is this item?")
cost = float(cost)
time = (input("Do you buy this item weekly, monthly, or yearly?"))
often_spent(time)
    


# Want_to_know = input("")

# if input :
#     print("")
    
    
        