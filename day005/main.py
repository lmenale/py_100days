# Using the for loop with Python Lists
fruits = ["Cherry", "Apple", "Pear"]
for fruit in fruits:
  print(fruit)

# For loops and the range() function
# Gauss example
# 1   2  3  ... 98 99 100
# 100 99 98 ... 3  2  1
# 50 (couple) * 101 (sum)
print("Gauss problem")
total = 0
for number in range(1, 101):
  total += number
print(total)

# Fizz Buzz
print("Fizz Buzz problem")
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    # Divisble by both 3 and 5
    print("FizzBuzz")
  elif number % 3 == 0:
    # Divisib1e by 3
    print("Fizz")
  elif number % 5 == 0:
    # Divisible by 5
    print("Buzz")
  else:
    print(number)
