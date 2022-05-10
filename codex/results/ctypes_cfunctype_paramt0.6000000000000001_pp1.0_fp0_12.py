import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte)

@FUNTYPE
def func(a, b):
    return a + b

def test_func(func):
    print(func(1, 2))

test_func(func)
</code>
The above code works.
But when I try to use it in my code:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte)

class MyClass:
    def __init__(self):
        self.func = FUNTYPE(self.func_impl)

    def func_impl(self, a, b):
        return a + b

def test_func(func):
    print(func(1, 2))

inst = MyClass()
test_func(inst.func)
</code>
I get this error:
<code>Traceback (most recent call last):
  File "test.
