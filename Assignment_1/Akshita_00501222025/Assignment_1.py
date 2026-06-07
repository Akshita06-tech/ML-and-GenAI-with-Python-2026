#NAME:AKSHITA
#ENROLLMENT_NO:00501222025
#COLLEGE_NAME:IGDTUW


# Question 1: Area of Rectangle
# =====================================
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area =", area)



# Question 2: Simple Interest
# =====================================

principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))
si = (principal * rate * time) / 100
print("Simple Interest =", si)


# Question 3: Celsius to Fahrenheit
# =====================================
celsius = float(input("Enter Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit =", fahrenheit)


# Question 4: Average of 3 Numbers
# =====================================
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("Average =", average)


# Question 5: Square and Cube of a Number
# =====================================
number = float(input("Enter a number: "))
square = number ** 2
cube = number ** 3
print("Square =", square)
print("Cube =", cube)


# Question 6: Swap Two Numbers Without Third Variable
# =====================================
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)


# Question 7: Student Report Program
# =====================================

# Taking student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Taking marks of 3 subjects
marks1 = float(input("Enter marks of Subject 1: "))
marks2 = float(input("Enter marks of Subject 2: "))
marks3 = float(input("Enter marks of Subject 3: "))

# Calculating total and percentage
total = marks1 + marks2 + marks3
percentage = (total / 300) * 100

# Displaying report
print("\n===== STUDENT REPORT =====")
print("Student Name:", name)
print("Roll Number:", roll_no)
print("Subject 1 Marks:", marks1)
print("Subject 2 Marks:", marks2)
print("Subject 3 Marks:", marks3)
print("Total Marks:", total)
print("Percentage:", percentage, "%")