# pgm4
 # Python program for Addition and Subtraction

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing addition
addition = num1 + num2

# Performing subtraction
subtraction = num1 - num2

# Displaying results
print("\nResults:")
print("Addition =", addition)
print("Subtraction =", subtraction)

multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"
print("Multiplication =", multiplication)
print("Division =", division)
  
