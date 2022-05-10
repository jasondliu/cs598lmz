import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def fn():
    return 1

x = fun
x()
# array(42, dtype=object)

a = np.frompyfunc(x,1,1)
a(fn(),fn())

# array(42, dtype=object)
#####################
# dtype=int
def x():
    return 42
a = np.frompyfunc(x,1,1)
a(fn(),fn())

# array(42, dtype=int)
</code>
Special functions:
<code># create a special function
a = np.frompyfunc(x,1,1)

# create another one from the same function and another dtype
b = np.frompyfunc(x,1,1,dtype=int)

# both functions still return the same value
a(fn(),fn())

# array(42, dtype=object)
b(fn(),fn())

# array(42, dtype=int)
</code>
My question is:
Why is this required in the first place?
Sure, many
