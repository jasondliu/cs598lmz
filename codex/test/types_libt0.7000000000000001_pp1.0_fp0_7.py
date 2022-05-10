import types
types.FunctionType

# __dict__
def myDict(myClass):
    return myClass.__dict__

class MyClass(object):
    def __init__(self):
        self.a = 2
        self.b = 'test'

mc = MyClass()
assert myDict(mc) == {'a':2, 'b':'test'}

# __class__
def myClass(myClass):
    return myClass.__class__

assert myClass(mc) == MyClass

# __name__
def myName(myClass):
    return myClass.__name__

assert myName(MyClass) == 'MyClass'

# __bases__
def myBases(myClass):
    return myClass.__bases__

assert myBases(MyClass) == (object,)

# __doc__
def myDoc(myClass):
    return myClass.__doc__

assert myDoc(MyClass) == None

class MyClass2(object):
    'my doc'

