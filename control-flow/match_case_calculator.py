num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print("The result is", result)
    
elif operation == "-":
    result = num1 - num2
    print("The result is", result)
    
elif operation == "*":
    result = num1 * num2
    print("The result is", result)
    
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("The result is", result)
    else:
        print("Cannot divide by zero.")