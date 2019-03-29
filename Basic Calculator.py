# User input of first and second number, with their selected operator
num1 = float(raw_input("Enter your first number: "));
opt = raw_input("Enter your operator: ");
num2 = float(raw_input("Enter your second number: "));


# output based on user input
if opt == "+":
    print (num1 + num2);
elif opt == "-":
    print (num1 - num2);
elif opt == "/":
    print (num1 / num2);
elif opt == "*":
    print (num1 * num2);
else:
    print ("Invalid operator");