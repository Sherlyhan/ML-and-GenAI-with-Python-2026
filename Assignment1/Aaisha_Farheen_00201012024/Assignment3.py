
# 1. FUNCTION TO PRINT FIRST 10 NATURAL NUMBERS

def print_natural_numbers():
    for i in range(1, 11):
        print(i, end=" ")
    print()

print("First 10 Natural Numbers:")
print_natural_numbers()


# 2. FUNCTION TO CALCULATE SUM OF FIRST N
# NATURAL NUMBERS

def sum_natural_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

n = int(input("\nEnter N: "))
print("Sum =", sum_natural_numbers(n))


# 3. FUNCTION TO REVERSE A NUMBER

def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse

num = int(input("\nEnter a Number: "))
print("Reversed Number =", reverse_number(num))


# 4. FUNCTION TO COUNT DIGITS IN A NUMBER

def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return count

num = int(input("\nEnter a Number: "))
print("Number of Digits =", count_digits(num))


# 5. FUNCTION TO CHECK PALINDROME NUMBER

def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return original == reverse

num = int(input("\nEnter a Number: "))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


# 6. FUNCTION TO GENERATE FIBONACCI SERIES

def fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci Series:")

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

    print()

n = int(input("\nEnter Number of Terms: "))
fibonacci(n)


# 7. CALCULATOR USING FUNCTIONS

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = float(input("\nEnter First Number: "))
num2 = float(input("Enter Second Number: "))

operation = input("Enter Operation (+, -, *, /): ")

if operation == "+":
    print("Result =", add(num1, num2))

elif operation == "-":
    print("Result =", subtract(num1, num2))

elif operation == "*":
    print("Result =", multiply(num1, num2))

elif operation == "/":
    print("Result =", divide(num1, num2))

else:
    print("Invalid Operation")


# 8. CREATE A TEXT FILE AND STORE STUDENT
# DETAILS

name = input("\nEnter Student Name: ")
roll_no = input("Enter Roll Number: ")

file = open("student.txt", "w")

file.write("Student Name: " + name + "\n")
file.write("Roll Number: " + roll_no)

file.close()

print("Student details saved in student.txt")


# 9. READ DATA FROM A FILE

file = open("student.txt", "r")

print("\nContents of File:")
print(file.read())

file.close()


# 10. HANDLE DIVISION BY ZERO USING
# EXCEPTION HANDLING

try:
    a = int(input("\nEnter Numerator: "))
    b = int(input("Enter Denominator: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by Zero is Not Allowed")


# 11. CREATE A STUDENT CLASS WITH NAME
# AND MARKS

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Marks:", self.marks)

name = input("\nEnter Student Name: ")
marks = float(input("Enter Marks: "))

s1 = Student(name, marks)

s1.display()