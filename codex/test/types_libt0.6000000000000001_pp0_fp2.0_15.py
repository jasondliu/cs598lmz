import types
types.ClassType

class ClassType: pass

def f():
    return ClassType()

f()

a = ClassType()

a.__class__

ClassType.__bases__

ClassType.__name__


class DerivedClass(ClassType):
    def f(self):
        return 'hello world'

dc = DerivedClass()

dc.f()


def f(self):
    return 'hello world'

DerivedClass = ClassType()
DerivedClass.f = f


DerivedClass.__dict__

dc = DerivedClass()
dc.f()


class DerivedClass(ClassType):
    def f(self):
        return 'hello world'

dc = DerivedClass()
dc.f()

def f(self):
    return 'hello world'

DerivedClass = ClassType()
DerivedClass.f = f

dc = DerivedClass()
dc.f()

def f(self):
    return 'hello world'

DerivedClass = ClassType()
