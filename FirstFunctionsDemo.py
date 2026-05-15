
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def add():
    result = num1 + num2
    print("The added value result is: ", result)

def sub():
    result = num1 - num2
    print("The substracted value result is: ", result)

def div():
    result = num1 / num2
    print("The dividing value result is: ", result)

def mult():
    result = um1 * num2
    print("The multiplying value result is: ", result)

def invalid():
    print("Invalid input. Please select a valid operation using numbers from 1 - 4")

def calculator():
    print("\n**** Available Operation **** \n 1. Addition \n 2. Substraction \n 3. Division \n 4. Multiplication \n")
    operation = int(input("Enter the number of operation you want to do: "))
    if (operation == 1):
        add()
    elif (operation == 2):
        sub()
    elif (operation == 3):
        div()
    elif (operation == 4):
        mult()
    else:
        invalid()

calculator()









   