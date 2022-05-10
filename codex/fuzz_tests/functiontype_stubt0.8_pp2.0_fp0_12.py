from types import FunctionType
a = (x for x in [1])
print type(a)
print type(a.next)
print dir(a.next)
print type(dir)
print type(dir())

# print a.next()
# print a.next()
# print a.next()

'''
class Test():
    def __init__(self):
        pass
    def add(self,x,y):
        return x+y

class Test2(Test):
    def __init__(self):
        pass
    def add(self):
        return super(Test2,self).add(1,2)

obj = Test2()
print dir(Test)
'''

'''
class Test(object):
    def __init__(self):
        pass
    def add(self,x,y):
        return x+y

class Test2(Test):
    def __init__(self):
        pass
    def add(self):
        return super(Test2,self).add(1,2)

obj = Test2()
'''

'''
import sys
print type(
