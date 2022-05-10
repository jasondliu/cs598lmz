import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 3

print fun()
</code>
I get the following error:
<code>TypeError: 'int' object is not callable
</code>
How could I make <code>fun</code> return a Python integer?


A:

Your function works fine. The problem is that you're trying to call <code>fun</code> after the function has exited. You have created a <code>FUNTYPE</code> object, but have not assigned it to a variable. Because the <code>fun</code> variable is created inside of a function, it's local to that function, and when that function exits, the variable <code>fun</code> goes away (is garbage collected).
To fix this, you need to assign <code>fun</code> to a variable outside the function, so that the variable still exists when the function exits:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

# Assign the function to a variable
fun = FUNTYPE(lambda: 3)

print fun()
# Output
3
</code>

