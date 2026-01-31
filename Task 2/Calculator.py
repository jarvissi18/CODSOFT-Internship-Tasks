# This is My Calculator using Python

num1 = float(input("Enter The First Number: "))
num2 = float(input("Enter The Second Number: "))

print("\n--- Choose The Operation ---")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

operation = input("Enter The Operation: ")

if operation == "+":
    print("The Result is =", num1 + num2)

elif operation == "-":
    print("The Result is =", num1 - num2)

elif operation == "*":
    print("The Result is =", num1 * num2)

elif operation == "/":
    if num2 != 0:
        print("The Result is =", num1 / num2)
    else:
        print("Error! Division by zero is not allowed..")

else:
    print("Invalid operation selected..")
