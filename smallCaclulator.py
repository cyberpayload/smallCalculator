# ********** A VERY SMALL CALULATOR **********

# define a function that accepts two arguements, both numbers that the user will provide for the math operation

while True:

    def smallCalculator(num1, num2, string):
        if string == '1':
            print('\n' + str(num1) + " + " + str(num2) + " = ", (num1 + num2))
        elif string == '2':
            print(str(num1) + " - " + str(num2) + " = ", (num1 - num2))
        elif string == '3':
            print(str(num1) + " * " + str(num2) + " = ", (num1 * num2))
        elif string == '4':    
            print(str(num1) + " / " + str(num2) + " = ", (num1 / num2))
        print("-------")

        quit = str(input('Quit? (Y/N)'))
    if quit == str('y') or quit  == str('Y'):
        break
    else:
        a = int(input('\n' + 'Enter 1st number: '))
        b = int(input('Enter 2nd number: '))
        oper = str(input("Type:\n(1) to Add\n(2) to Subtract\n(3) to Multiply\n(4) to Divide\n"))
        smallCalculator((a), (b), (oper))