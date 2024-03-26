# Random Module
import random

random_integer = random.randint(1, 10)
print(random_integer)
random_float = random.random()
print(random_float)

# Understanding the Offset and Appending Items to Lists
fruits = ["Cherry", "Apple", "Pear"] # They are ordered starting from element 0 = Cherry ...
print(fruits[1])
print(fruits[-1])
# To add use "append"
fruits.append("Melon")

# Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
num_items = len(names)
#Generate random numbers between and the last index.
# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]

person_who_will_pay = random.choice(names)
print (person_who_will_pay + " is going to buy the meal today! ")

# Index Errors and Working with Nested Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
