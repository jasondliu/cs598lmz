import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def my_callback(x, y):
    return x + y

my_callback_c = FUNTYPE(my_callback)

my_callback_c(1, 2)
</code>
The above code works, but I want to use <code>my_callback</code> as a class method. I tried the following, but it does not work.
<code>class MyClass(object):
    def __init__(self):
        pass

    def my_callback(self, x, y):
        return x + y

my_callback_c = FUNTYPE(MyClass.my_callback)

my_callback_c(1, 2)
</code>
The error is:
<code>TypeError: must be convertible to a pointer
</code>
I know I can do the following, but I want to use the class method directly without creating an instance of <code>MyClass</code>.
<code>class MyClass(object):
    def __init__(self):
        pass


