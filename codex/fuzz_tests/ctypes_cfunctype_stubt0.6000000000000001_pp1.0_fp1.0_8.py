import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"
print(fun())
</code>
This will print
<code>Hello World
</code>
What I am doing is using <code>ctypes</code> to define a <code>CFUNCTYPE</code> that returns a <code>py_object</code>, and then just returns a string.
However, if you want to call a function written in C, you can use <code>ctypes</code> as well. Here is an example of how to do that:
<code>import ctypes

print(ctypes.CDLL('./libfoo.so').foo())
</code>
Where <code>libfoo.so</code> is the name of the shared object library you want to load.

