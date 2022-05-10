from types import FunctionType
list(FunctionType(list,list,list))
"""

"""
class A(object):
    def __init__(self):
        self.a = 1

b=A()
b.__getattr__()
"""

"""
class A(object):
    def __init__(self):
        self.a = 1
    def __setattr__(self, name, value):
        print 'setattr'
        self.__dict__[name] = value

b=A()
b.__setattr__('a',2)
"""

"""
class Foo:
    pass
def func1(self):
    print "func1"
f=Foo()
f.func2=func1
f.func2()
setattr(Foo,'func2',func1)
f=Foo()
f.func2()
"""

"""
class Foo:
    pass
def func1(self):
    print "func1"
f=Foo()
f.func2=func1
f.func2()
setattr(Foo,'func2',func1)
