# User input of first and second number, with their selected operator
num1 = float(input("Enter your first number: "))
opt = input("Enter your operator: ")
num2 = float(input("Enter your second number: "))


# output based on user input
if opt == "+":
    print (num1 + num2)
elif opt == "-":
    print (num1 - num2)
elif opt == "/":
    print (num1 / num2)
elif opt == "*" or opt == "x" or opt == "X":
    print (num1 * num2)
else:
    print ("Invalid operator")