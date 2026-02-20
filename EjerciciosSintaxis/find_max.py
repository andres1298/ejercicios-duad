# Exercise 4: Max of Three Numbers (Simplified)

print("--- Find the Largest Number ---")

# Ask for three numbers (will fail if not numbers)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Compare them
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Display the result
print(f"\nThe largest number among {num1}, {num2}, and {num3} is: {largest}")
