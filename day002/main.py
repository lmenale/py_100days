# Python Primitive Data Types and Data Types
# String
print("Holidays"[2] + " - array index start from 0")
print(type("12345"))
# Integer
large_int = 1_985_624
print(int("561") + 1)
print(type(large_int))
# Float
float_number = 3.14159
print(float("5.61") + 1.05)
print(type(float_number))
# Boolean (True or False)
check = 1 > 2
print(check)
# Type Error, Type Checking and Type Conversion
num_char = len(input("What is your name?"))
# print(" Your name has " + num_char + " characters.") # TypeError
print(" Your name has " + str(num_char) + " characters.") # All strings

# Mathematical Operations in Python (PEMDAS)
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
print(8 // 3) # Integer division

# Number Manipulation and F Strings in Python
print(f"Integer: {large_int}, Float: {float_number}, Boolean: {check}")
print("Float: {:.2f}".format(float_number))
