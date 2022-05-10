from types import FunctionType
list(FunctionType(lambda x: x * 2, globals(), 'foo') for x in range(10))

# __code__
def foo():
    pass
foo.__code__.co_code
foo.__code__.co_filename
foo.__code__.co_argcount
foo.__code__.co_varnames

# __class__
(1).__class__

# __debug__
__debug__

# __delattr__
class A:
    def __delattr__(self, name):
        print('Deleting', name)
        super().__delattr__(name)
a = A()
a.x = 5
del a.x

# __delitem__
class A:
    def __delitem__(self, index):
        print('Deleting', index)
        super().__delitem__(index)
a = A()
a[0] = 5
del a[0]

# __dict__
class A:
    pass
a = A()
a.__dict__

# __dir__
class A:
