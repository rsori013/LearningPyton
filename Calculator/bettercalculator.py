
num1 = float(input("Enter a number: "))
operation = str(input("Enter a operation: "))
num2 = float(input("Enter a number2: "))


if(operation == "+"):
    num1 = float(num1 + num2)
elif(operation == "-"):
    num1 = float(num1 - num2)
elif(operation == "*"):
   num1 = float(num1 * num2)
elif(operation == "/"):
    num1 = float(num1 / num2)
else:
    print("Invalid operation")

print(num1)
