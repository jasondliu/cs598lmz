import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)
def func(a, b):
    return a + b
func_ptr = FUNTYPE(func)

class MyClass(ctypes.Structure):
    _fields_ = [("data", ctypes.c_double),
                ("func", FUNTYPE)]

my_class = MyClass()
my_class.data = 1.0
my_class.func = func_ptr

print my_class.func(2.0, 3.0)
</code>
This prints
<code>5.0
</code>

