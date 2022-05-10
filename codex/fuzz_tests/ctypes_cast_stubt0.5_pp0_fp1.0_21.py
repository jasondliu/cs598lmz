import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
I get the following error:
<code>TypeError: cannot be converted to a pointer
</code>
So, how can I cast an object to a pointer?


A:

You can't. 
What you can do is to use a <code>ctypes.c_void_p</code> (or <code>ctypes.c_void_p*1</code> if you need an array of pointers) and set the value to the address of your object.
<code>import ctypes

class X(object):
    pass

x = X()

v = ctypes.c_void_p()
v.value = id(x)

print(ctypes.cast(v, ctypes.py_object).value)
# &lt;__main__.X object at 0x7f6e8a6b86d0&gt;
</code>

