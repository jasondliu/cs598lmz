from types import FunctionType
list(FunctionType(FunctionType.__code__, globals(), 'foo').__closure__)

# Issue #5716: Check that the __closure__ attribute is not writable.
def f():
    def g():
        pass
    g.__closure__ = (1, 2, 3)

try:
    f()
except TypeError:
    pass
else:
    print('__closure__ is writable')

# Issue #5716: Check that the __code__ attribute is not writable.
def f():
    def g():
        pass
    g.__code__ = (1, 2, 3)

try:
    f()
except TypeError:
    pass
else:
    print('__code__ is writable')

# Issue #5716: Check that the __defaults__ attribute is not writable.
def f():
    def g(a=1):
        pass
    g.__defaults__ = (2, 3)

try:
    f()
except TypeError:
    pass
else:
    print('__defaults__ is writable')


