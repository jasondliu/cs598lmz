import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("I got called with %d and %d" % (a, b))
    return a + b

callback = FUNTYPE(my_callback)

# call the function, passing the callback as an argument
print(mylib.call_me(callback))

# call the function, passing the callback as an argument
print(mylib.call_me(callback))
</code>
The output is:
<code>I got called with 1 and 2
I got called with 3 and 4
3
I got called with 5 and 6
5
</code>

