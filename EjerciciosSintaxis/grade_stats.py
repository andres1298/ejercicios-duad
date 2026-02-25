# Exercise 5: Grade Statistics (Simplified)

print("--- Grade Statistics Calculator ---")
n = int(input("How many grades would you like to enter? "))

grades = []

# Loop for the specified amount of grades
for i in range(n):
    grade = float(input(f"Enter grade {i+1}: "))
    grades.append(grade)

# Statistics logic
approved_grades = [g for g in grades if g >= 70]
disapproved_grades = [g for g in grades if g < 70]

count_approved = len(approved_grades)
count_disapproved = len(disapproved_grades)

# Calculate averages (Note: will fail if no approved/disapproved grades)
avg_all = sum(grades) / len(grades)
avg_approved = sum(approved_grades) / count_approved
avg_disapproved = sum(disapproved_grades) / count_disapproved

# Display results
print("\n--- Statistics ---")
print(f"Total grades entered: {len(grades)}")
print(f"Approved grades: {count_approved}")
print(f"Disapproved grades: {count_disapproved}")
print(f"Average of all grades: {avg_all:.2f}")
print(f"Average of approved: {avg_approved:.2f}")
print(f"Average of disapproved: {avg_disapproved:.2f}")
