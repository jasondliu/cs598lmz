import types
types.ClassType = 2
from types import *

class Array:
    def __init__(self, size):
        self.size = size
        self.array = []
        self.seed = randint(1, self.size)

    def add(self, el):
        if self.seed < self.size:
            self.array.append(el)
            self.seed = randint(1, self.size)
        else:
            self.seed = randint(1, self.size)
            self.array[self.seed] = el

    def __str__(self):
        return str(self.array)

if __name__=='__main__':
    test = Array(10)
    for el in xrange(10):
        test.add((randint(1,10), randint(1,10)))
    print test
