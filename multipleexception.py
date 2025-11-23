try:
    num1,num2=eval(input("Enter 2 numbers Seprated by comma:"))
    result= num1/num2
    print("Result is :",result)
except ZeroDivisionError as ex:
    print("Division by zero is an error",ex)
except SyntaxError as ex:
    print("Comma is missing. Enter number seprated by comma like 1 , 2")
except ValueError as ex:
    print("Wrong input")
else:
    print("No exception")
