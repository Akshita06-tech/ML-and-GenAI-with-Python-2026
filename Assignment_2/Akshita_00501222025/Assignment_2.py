#NAME:AKSHITA
#ENROLLMENT_NO:00501222025
#COLLEGE_NAME:IGDTUW

# 1. Find sum of first 10 natural numbers
# =====================================
sum = 0
for i in range(1, 11):
    sum+= i
print("1. Sum of first 10 natural numbers:", sum)


# 2. Find factorial of a number
# =====================================
num = int(input("Enter a number to find factorial: "))
fact = 1

if num < 0:
    print("Factorial not defined for negative numbers")
else:
    for i in range(1, num + 1):
        fact *= i
    print("Factorial of", num, "is:", fact)


# 3. Print Fibonacci Series
# =====================================
n = int(input("Enter number of terms for Fibonacci series: "))
a, b = 0, 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# 4. Find largest among 3 numbers
# =====================================
print("Find largest among 3 numbers")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Largest number is:", largest)


# 5. Create Student Result System
# =====================================
print("\n5. Student Result System")
name = input("Enter student name: ")
roll = input("Enter roll number: ")
total_marks = 0
subjects = 5
for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks for subject {i}: "))
    total_marks += marks
percentage = total_marks / subjects
print("Percentage:", percentage)
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"
print("Student Result :  ")
print("Name:", name)
print("Roll No:", roll)
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)