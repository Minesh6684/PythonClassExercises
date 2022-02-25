# Greeting a user using function

def greet(name):
    print(f'Hello, {name}')


greet(name=input('Enter your name: '))

# Get factorial of a number using function


def get_factorial(number):
    output = number
    for i in range(1, number):
        output *= i
    return f'{number}! = {output}'


print(get_factorial(5))
