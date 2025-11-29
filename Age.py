try:
    num1=eval(input("Enter your age :"))
    if (num1 % 2 == 0):
        print("Your age is even")
    else:
        print("Your age is odd")
except ZeroDivisionError as ex:
    print("Division by zero is an error",ex)
except SyntaxError as ex:
    print("Comma is missing. Enter number seprated by comma like 1 , 2")
except ValueError as ex:
    print("Wrong input")
else:
    print("No exception")