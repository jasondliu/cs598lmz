import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello world")

fun()
</code>
I get the following error:
<code>ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: wrong type
</code>
What am I doing wrong?


A:

<code>ctypes</code> is a bit confusing here.
The <code>CFUNCTYPE</code> class is a factory for creating C function pointers, not Python function objects.
You can create a function pointer by passing the <code>restype</code> and <code>argtypes</code> arguments to the <code>CFUNCTYPE</code> constructor:
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
</code>
Once you have a function pointer, you can assign it to a global variable, or pass it to a function, or call it directly.
<code># Define a global variable
add = FUNTYPE(lambda x, y: x + y)

# Pass it to a function

