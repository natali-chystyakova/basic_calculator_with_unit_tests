
import math
class Calculator():
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        if not isinstance(other, Calculator):
            raise TypeError("Operands must be Calculator instances")

        if not isinstance(self.x, (int, float)) or not isinstance(other.x, (int, float)):
            raise TypeError("Operands must be of compatible types")

        z = self.x + other.x

        return Calculator(z)



    def __sub__(self, other):
        if not isinstance(other, Calculator):
            raise TypeError("Operands must be Calculator instances")

        if not isinstance(self.x, (int, float)) or not isinstance(other.x, (int, float)):
            raise TypeError("Operands must be of compatible types")

        z = self.x - other.x

        return Calculator(z)



    def __mul__(self, other):
        if not isinstance(other, Calculator):
            raise TypeError("Operands must be Calculator instances")

        if not isinstance(self.x, (int, float)) or not isinstance(other.x, (int, float)):
            raise TypeError("Operands must be of compatible types")

        z = self.x * other.x

        return Calculator(z)


    def __truediv__(self, other):
        if not isinstance(other, Calculator):
            raise TypeError("Operands must be Calculator instances")

        if not isinstance(self.x, (int, float)) or not isinstance(other.x, (int, float)):
            raise TypeError("Operands must be of compatible types")
        if other.x == 0:
            raise ZeroDivisionError("--Division by zero--")

        z = self.x / other.x
        return Calculator(z)


    def __pow__(self, other):
        if not isinstance(other, Calculator):
            raise TypeError("Operands must be Calculator instances")

        if not isinstance(self.x, (int, float)) or not isinstance(other.x, (int, float)):
            raise TypeError("Operands must be of compatible types")

        if other.x < 0:
            raise ValueError("Exponent must be non-negative")

        z = self.x ** other.x
        return Calculator(z)


    def sqrt(self):

        if not isinstance(self.x, (int, float)) :
            raise TypeError("Operands must be of compatible types")

        if self.x < 0:
            raise ValueError("Cannot extract square root from negative number")

        z = math.sqrt(self.x)
        return Calculator(z)

    def __str__(self):
        return str(self.x)





# если тесты и программа в одном файле:
# if __name__=='__main__':
#     import doctest
#     doctest.testmod()


# если тесты в отдельном файле:
if __name__=='__main__':
    import doctest
    doctest.testfile("class_calculator_doctests.txt")

# запуск doctest через коммандную строку:
# python -m doctest -v class_calculator_doctests.txt

