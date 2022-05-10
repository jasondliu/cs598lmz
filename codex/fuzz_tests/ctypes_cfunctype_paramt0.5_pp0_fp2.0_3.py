import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

class A(object):
    def __init__(self):
        self.f = FUNTYPE(self.foo)

    def foo(self, a):
        return a

a = A()

def bar(f):
    print f(1)

bar(a.f)
</code>

<code>$ python test.py
1
</code>

