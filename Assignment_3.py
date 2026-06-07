#NAME:AKSHITA
#ENROLLMENT_NO:00501222025
#COLLEGE_NAME:IGDTUW

# 1. Function to print first 10 natural numbers
# ==============================================

def print_first_10():
    for i in range(1, 11):
        print(i, end=" ")
    print()

print("1. First 10 natural numbers:")
print_first_10()


# 2. Function to calculate sum of first N natural numbers
# ==============================================
def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("2. Enter N: "))
print("Sum of first", n, "natural numbers:", sum_natural(n))


# 3. Function to reverse a number
# ==============================================
def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + (num % 10)
        num //= 10
    return rev

num = int(input("3. Enter number to reverse: "))
print("Reversed number:", reverse_number(num))


# 4. Function to count digits
# ==============================================
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count
num = int(input("\n4. Enter number to count digits: "))
print("Number of digits:", count_digits(num))


# 5. Function to check palindrome
# ==============================================
def is_palindrome(num):
    original = num
    rev = 0
    while num > 0:
        rem = num % 10        # get last digit
        rev = rev * 10 + rem  # build reverse
        num = num // 10       # remove last digit
    if original == rev:
        return True
    else:
        return False
num = int(input("\nEnter number to check palindrome: "))
if is_palindrome(num):
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")


# 6. Function to generate Fibonacci series
# ==============================================
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
terms = int(input("6. Enter number of terms for Fibonacci: "))
print("Fibonacci Series:")
fibonacci(terms)


# 7. Calculator using functions
# ==============================================
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

print("7. Calculator")
print("1.Add  2.Subtract  3.Multiply  4.Divide")
choice = int(input("Enter your choice: "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if choice == 1:
    print("Result:", add(a, b))
elif choice == 2:
    print("Result:", subtract(a, b))
elif choice == 3:
    print("Result:", multiply(a, b))
elif choice == 4:
    print("Result:", divide(a, b))
else:
    print("Invalid choice")


# 8. Create a text file and store student details
# ==============================================
print("8. Writing student data to file")
with open("students.txt", "w") as f:
    n = int(input("How many students: "))
    for i in range(n):
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        f.write(name + "," + marks + "\n")
print("Data saved in students.txt")


# 9. Read data from file
# ==============================================
print("9. Reading data from file")
try:
    with open("students.txt", "r") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("File not found!")


# 10. Handle division by zero (separate example)
# ==============================================
print("10. Division with exception handling")
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    print("Result:", x / y)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")


# 11. Student class
# ==============================================
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

print("\n11. Student Class Example")
name = input("Enter student name: ")
marks = input("Enter marks: ")
s1 = Student(name, marks)
s1.display()
