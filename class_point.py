"""
>>> a=Point(0, 0)
>>> b=Point(1, 6)
>>> c= a+b
>>> print(c)
Point(1, 6)
>>> b.distance_from_origin()
6.082762530298219
"""

import math
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return (f"Point({self.x}, {self.y})")

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)





# если тесты и программа в одном файле:
if __name__=='__main__':
    import doctest
    doctest.testmod()