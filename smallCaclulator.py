# ********** A VERY SMALL CALULATOR **********

# define a function that accepts two arguements, both numbers that the user will provide for the math operation
def smallCalculator(num1, num2):
    print(str(num1) + " + " + str(num2) + " = ", (num1 + num2))


a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

smallCalculator((a), (b))