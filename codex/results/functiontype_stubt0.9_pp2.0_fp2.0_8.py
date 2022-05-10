from types import FunctionType
a = (x for x in [1])
print(type(a))
print(next(a))
print(next(a))
'''
#0.0.05 ________________________
'''
class objectCreator(object):
    pass
my_object = objectCreator()
print(my_object)
print(my_object.__class__)
print(objectCreator)
print(objectCreator.__class__)
'''
#0.0.04 ________________________
'''
import time
t = time.clock()
class A(object):
    def __init__(self):
        self.x = 1
        self.y = 2
    def fgh(self, j):
        return self.x + self.y + j
t2 = time.clock() - t

class A(object):
    x = 1
    y = 2
    def fgh(self,j):
        return self.x + self.y + j

t1 = time.clock() - t2
print('1-', t1)
print('2-', t2)
'''
#0.0
