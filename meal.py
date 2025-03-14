#meal price calculator program
#this program prompts the user to enter the price of a meal, the tax rate, and the tip rate
#it then calculates the total price of the meal and prints it out
print("welcome to the meal price calculator program")
print("answer the following questions to calculate the total price of your meal")  
#prompt the user for input and saving to variables
meal_1_price = float(input("Enter the price of the meal: "))
meal_2_price = float(input("Enter the price of the second meal: "))
tax_rate = float(input("Enter the tax rate: "))
tip_rate = float(input("Enter the tip rate: "))
#prommpt the user for quantities of each meal
meal_1_quantity = float(input("Enter the quantity of the first meal: "))
meal_2_quantity = float(input("Enter the quantity of the second meal: "))
#calculate the total meal price
meal_price = meal_1_price + meal_2_price
#calculate the tax and tip
tax = meal_price * tax_rate
tip = meal_price * tip_rate
#calculate the total price
total_price = meal_price + tax + tip
# calculate the total quantity
total_quantity = meal_1_quantity + meal_2_quantity
#calculate total amount
total_amount = meal_1_price * meal_1_quantity + meal_2_price * meal_2_quantity
#prompt the user for the payment amount
payment = float(input("Enter the payment amount: "))
#calculate the change
change = payment - total_price
#Display the results with proper formatting
print("The total price of the meal is: $" + str(total_price))
print("The total quantity of the meal is: " + str(total_quantity)) 
print("The total amount of the meal is: $" + str(total_amount))
print("The change is: $" + str(change))
#output the total price
print("The total price of the meal is: $" + str(total_price))
#end of program
print("Thank you for using the meal price calculator program")
# End of Path: meal.py