from types import FunctionType
list(FunctionType(int, int))

FunctionType(int, int)(1)

def f(): pass

FunctionType(int, int)(1)

# Test that classes can be called

class C(object):
    def __init__(self, arg1, arg2='default'):
        pass

C('hello', 'world')
C(1, 2)
C(1.1, 2.2)
C(object())
C('hello', arg2 = 'world')
C(arg1 = 'hello', arg2 = 'world')
C(arg2 = 'world', arg1='hello')
C(arg1 = 'hello')
# The previous line raises a stack overflow under CPython
# which was fixed by removing polymorphic dispatch for __init__.
C('hello', arg2 = 'world', extra='ignored')
C('hello', arg1 = 'ignored')
C(arg2 = 'ignored', arg1='hi')
try:
    C()
except TypeError:
    print "TypeError"
try:
    C(1, 2, 3)
except Type
