import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello world"

print(fun())
</code>
The error is: 
<blockquote>
<p>WindowsError: exception: access violation writing 0x00000000</p>
</blockquote>
It works with a <code>c_int</code> return.
I suspect this is because creating the function has bound <code>fun</code> to an address in memory, which is not guaranteed to be the same address upon calling the function, if it has been garbage collected from the first call. Is there a way to ensure that the address does not change?


A:

A <code>CFUNCTYPE</code> instance is not a callable. It's a factory for callable functions. You have to call the <code>CFUNCTYPE</code> instance first to get a function object.
<code>print(fun()) # prints None

fun_func = fun() # creates the function
print(fun_func()) # prints Hello World
print(fun_func()) # prints Hello World again
</code>

