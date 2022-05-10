import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hi"
</code>
This does not work, because the return value is a pointer to the string object, not the string itself, so I get the following error:
<code>ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: expected LP_c_char instance instead of str
</code>
I've tried adding <code>ctypes.POINTER(ctypes.c_char)</code> to the return type, but then I get a <code>TypeError</code> when I try to set the return value in the function:
<code>ctypes.ArgumentError: argument 2: &lt;class 'TypeError'&gt;: expected LP_c_char instance instead of str
</code>
How can I make a function that returns a string?

