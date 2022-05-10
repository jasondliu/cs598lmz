from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type([]))
print(type(abs))
print(type(FunctionType))

# FunctionType is the type of abs
print(type(lambda x: x))
print(type((x for x in range(10))))

# isinstance()
# isinstance(a, b) return true if a is an instance of b or is a subclass of b
# isinstance(a, b)
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance(100, Iterable))

# dir()
# if no args, return current module name
# if args, return args' attributes
print(dir('ABC'))
print('ABC'.__len__())
# getattr()
# getattr(object, name[, default])
# get attribute of object, if not found, return default
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
