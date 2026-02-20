# Exercise 2: Age Categorization (Simplified)

# Ask for user information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age_str = input("Enter your age: ")

# Convert age to integer directly (will fail if not a number)
age = int(age_str)

# Categorize based on age
if age < 0:
    category = "Invalid age"
elif age <= 2:
    category = "Baby"
elif age <= 12:
    category = "Child"
elif age <= 14:
    category = "Pre-teen"
elif age <= 17:
    category = "Teen"
elif age <= 30:
    category = "Young Adult"
elif age <= 64:
    category = "Adult"
else:
    category = "Senior"

# Display result
print(f"\nHello {first_name} {last_name}!")
print(f"Based on your age ({age}), you are categorized as: {category}")
