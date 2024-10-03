# creating the basic calculator program

operator=input("What operation do you want to perform? (+,-,*,/) ")

num1=int(input("Enter the first number: "))

num2=int(input("Enter the second number: "))

if operator=="+":
    print("you have chosen addition")
    print(num1+num2)
elif operator=="-":
    print("you have chosen subtraction")
    print(num1-num2)
elif operator=="*":
    print("you have chosen multiplication")
    print(num1*num2)
elif operator=="/":
    print("you have chosen division")
    print(num1/num2)
else:
    print("invalid operator")