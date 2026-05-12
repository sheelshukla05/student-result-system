# Student Result Management System

# Input student details
name = input("Enter student name: ")

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# Calculate total and percentage
total = mark1 + mark2 + mark3
percentage = total / 3

# Display result
print("\n----- RESULT -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

# Grade calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)

# Pass/Fail status
if percentage >= 40:
    print("Status: Pass")
else:
    print("Status: Fail")