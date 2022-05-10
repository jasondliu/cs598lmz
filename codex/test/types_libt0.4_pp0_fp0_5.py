import types
types.ClassType

class MyClass:
    pass

def MyFunc():
    pass

print(type(MyClass))
print(type(MyFunc))
print(type(MyFunc) == types.FunctionType)
print(type(MyClass) == types.ClassType)
print(type(MyClass))

print(type(1))
print(type(""))
print(type([]))
print(type({}))

print(type(1) == type(1.0))
print(type("") == type([]))
print(type("") == type(()))

print(type(1) == type(""))
print(type(1) == type([]))
print(type(1) == type({}))

print(type(1) == type(1.0))
print(type("") == type([]))
print(type("") == type(()))

print(type(1) == type(""))
print(type(1) == type([]))
print(type(1) == type({}))

