import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

# Python-side function, just prints a message and returns 1
def add(arg1, arg2):
    print("add called...")
    return arg1 + arg2

# Gets a pointer to a function which just prints a message
# and returns 1
add_func = FUNTYPE(add)
</code>
It works. I have followed the example, but I don't know...
<code># Python-side function, just prints a message and returns 1
def add(arg1, arg2):
    print("add called...")
    return arg1 + arg2

# Gets a pointer to a function which just prints a message
# and returns 1
add_func = FUNTYPE(add)
</code>
How to use the function? If I want to call it with 2 I need to do something like that?
<code>with open('my_lib.so', 'r') as f:
    my_lib = ctypes.cdll.LoadLibrary('my_lib.so')
</code>
I don't really understand the ctypes.CFUNCTYPE
