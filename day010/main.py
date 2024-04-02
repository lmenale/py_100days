# Function with Outputs
def is_Empty(name):
  if name == "":
    return True
  else:
    return False

# Multiple return values
def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers"
    elif number == 0:
        return 1
    else:
        factorial_value = 1
        for i in range(1, number + 1):
            factorial_value *= i
        return factorial_value

number = int(input("Enter a non-negative integer: "))
print("The factorial of", number, "is", factorial(number))

# Docstrings
# Print vs. Return
# While Loops, Flags and Recursion
def format_name( f_name, l_name):
   """Take a first and last name and format it to
   return the title case version of the name."""
   if f_name == "" or l_name == "":
      return "You didn't provide valid inputs."
   formated_f_name = f_name.title()
   formated_l_name = l_name.title()
   return f"Result: {formated_f_name} {formated_l_name}"

# Combining Dictionaries and Functions
def add(n1, n2):
   pass

def subtract(n1, n2):
   pass

operation = {
   "+": add,
   "-": subtract,
}

function = operation["+"]
function(2, 3)
