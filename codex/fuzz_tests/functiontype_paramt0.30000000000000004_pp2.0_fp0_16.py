from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'foo'))

# Test that the repr of a function is eval-able
def f():
    pass

repr(f)

# Test that the repr of a method is eval-able
class C:
    def m(self):
        pass

repr(C.m)

# Test that the repr of a builtin is eval-able
repr(len)

# Test that the repr of a method descriptor is eval-able
repr(int.__add__)

# Test that the repr of a member descriptor is eval-able
repr(int.real)

# Test that the repr of a wrapper descriptor is eval-able
repr(int.__new__)

# Test that the repr of a class is eval-able
repr(int)

# Test that the repr of a module is eval-able
repr(sys)

# Test that the repr of a code object is eval-able
repr(f.__code__)

# Test that the repr of a frame is eval-able
def g():

