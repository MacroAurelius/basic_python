# Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          return X if the condition is true, else return Y
#                          X if condition else Y

num = 5
#Checking to see if the number is positive
print("Positive" if num > 0 else "Negative")

#Check to see if the number is Even or Odd
num2 = 9
print(f"{num2} is EVEN" if num2 % 2 == 0 else f"{num2} is ODD")

#Or you can ASSIGN the condition
num3 = 6
result = "EVEN" if num3 % 2 == 0 else "ODD"
print(f"{num3} is {result}")

#Check maximum number value
a = 6
b = 7

max_num = a if a > b else b
print(f"{max_num} is the greater value!")

#Check minimum number value
min_num = a if a < b else b
print(f"{min_num} is the lesser value!")

#Check age for Adult or Child
age = 25

status = "Adult" if age >= 18 else "Child"
print(status)

#Check weather
temperature = 42
degree_symbol = "\u00b0"
weather = "HOT" if temperature > 68 else "COLD"
print(f"It is {temperature}{degree_symbol}, and it is {weather} outside")
# print(f"It is {temperature2}{degree_symbol}, and it is {weather} outside")


#Check the role of the user
user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(f"This user role is {user_role} and has {access_level}")

