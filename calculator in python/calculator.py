def addition(X, Y):
    return X + Y

def subtraction(X, Y):
    return X - Y

def multiplication(X, Y):
    return X * Y

def division(X, Y):
    if Y != 0:
        return X / Y
    else:
        return 'Error: Division by zero!'

def calculator():
    print('Choose an operation:\n')
    print('1 - Addition')
    print('2 - Subtraction')
    print('3 - Multiplication')
    print('4 - Division')

    operation = input('Choose the number of the operation (1,2,3,4): ')

    if operation in ['1', '2', '3', '4']:
        try:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
        except ValueError:
            print('Invalid input. Please enter numeric values.')
            return

        if operation == '1':
            print(f'{num1} + {num2} = {addition(num1, num2)}')
        
        elif operation == '2':
            print(f'{num1} - {num2} = {subtraction(num1, num2)}')
        
        elif operation == '3':
            print(f'{num1} * {num2} = {multiplication(num1, num2)}')
        
        elif (operation == '4'):
            print(f'{num1} / {num2} = {division(num1, num2)}')
    else:
        print('Invalid operation, try again!')

calculator()