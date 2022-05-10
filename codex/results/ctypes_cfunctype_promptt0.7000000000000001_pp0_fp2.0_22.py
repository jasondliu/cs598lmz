import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is not good enough: it just checks whether it crashes in the
# presence of ctypes. I'd like to check that it has the right effect, but
# how can I do that?
import sys
import weakref

def func(a, b):
    return a+b

class MyClass:
    pass

def func_ptr(x):
    print 'in func_ptr', x
    sys.stderr.write('test passed')
    sys.exit(0)

def callback(result, arg):
    print 'in callback', result, arg

def test_with_instancemethod():
    print 'testing instancemethod'
    t = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))
    x = MyClass()
    x.foo = t(func)
    print x.foo
    print x.foo(42)

def test_with_classmethod():
    print 'testing classmethod'
    t = ctypes.CFUNCTYPE(ctypes.c
