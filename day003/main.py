# Control Flow with if / else and Conditional Operators
condition = False
if condition:
  print("True condition")
else:
  print("False condition")

# Modulo Operator
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
  print("This is a even number.")
else:
  print("This is an odd number.")

# Nested if statements and elif statements
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
  print(f"Your bmi is {bmi}, you are obese.")
else:
  print(f"Your bmi is {bmi}, you are clinically obese.")

# Multiple If Statements in Succession
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print ("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print (f"Your final bill is {bill}")

else:
  print("Sorry, you have to grow taller before you can ride. ")

# Logical Operators
# Use the operator "and" "or" "not"