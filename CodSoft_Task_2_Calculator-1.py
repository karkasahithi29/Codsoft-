print("================================")
print("        SIMPLE CALCULATOR       ")
print("================================")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n----------- MENU -----------")
print("       +  Addition")
print("       -  Subtraction")
print("       *  Multiplication")
print("       /  Division")
print("----------------------------")

operation = input("Choose an operation: ")

if operation == "+":
    result = num1 + num2
    print("\nResult:", num1, "+", num2, "=", result)

elif operation == "-":
    result = num1 - num2
    print("\nResult:", num1, "-", num2, "=", result)

elif operation == "*":
    result = num1 * num2
    print("\nResult:", num1, "*", num2, "=", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("\nResult:", num1, "/", num2, "=", result)
    else:
        print("\nCannot divide by zero!")

else:
    print("\nInvalid operation!")

print("\n================================")
print("        Thank You! 😊")
print("================================")
