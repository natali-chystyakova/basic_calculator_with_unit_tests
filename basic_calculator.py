
import math

def addition(a, b):
    return a+b

def subtraction(a, b):
    return a-b

def multiplication(a, b):
    return a*b

def division(a, b):
    if b==0:
        raise ValueError("--Division by zero--")
    return a/b

def power(a, b):
    if b<0:
        raise ValueError("--Not available in basic calculator--")
    return math.pow(a, b)

def sqroot(a):
    if a < 0:
        raise ValueError("--Must be positive--")
    return math.sqrt(a)

# если тесты и программа в одном файле:
# if __name__=='__main__':
#     import doctest
#     doctest.testmod()

# запуск doctest через коммандную строку:
# python -m doctest -v basic_calculator.py


# если тесты в отдельном файле:
# if __name__=='__main__':
#     import doctest
#     doctest.testfile("doctests.txt")

# запуск doctest через коммандную строку:
# python -m doctest -v doctests.txt