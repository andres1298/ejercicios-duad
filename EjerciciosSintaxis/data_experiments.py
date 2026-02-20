# Exercise 1: Experimenting with Data Types (Simplified)

print("--- Python Data Type Experiments ---")

# 1. string + string
print("\n1. string + string:")
result1 = "Hello " + "World"
print(f'  "Hello " + "World" = {result1}')

# 2. string + int
# This will fail!
print("\n2. string + int:")
# result2 = "Age: " + 25
# print(f'  "Age: " + 25 = {result2}')
print("  (Code commented out because it causes a TypeError)")

# 3. int + string
# This will also fail!
print("\n3. int + string:")
# result3 = 10 + " apples"
# print(f'  10 + " apples" = {result3}')
print("  (Code commented out because it causes a TypeError)")

# 4. list + list
print("\n4. list + list:")
result4 = [1, 2] + [3, 4]
print(f"  [1, 2] + [3, 4] = {result4}")

# 5. string + list
# This will fail!
print("\n5. string + list:")
# result5 = "Items: " + [1, 2, 3]
# print(f'  "Items: " + [1, 2, 3] = {result5}')
print("  (Code commented out because it causes a TypeError)")

# 6. float + int
print("\n6. float + int:")
result6 = 5.5 + 10
print(f"  5.5 + 10 = {result6}")

# 7. bool + bool
print("\n7. bool + bool:")
result7 = True + True
print(f"  True + True = {result7}")

print("\n--- End of Experiments ---")
