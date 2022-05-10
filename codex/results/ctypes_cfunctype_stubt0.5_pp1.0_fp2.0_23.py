import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'
</code>
This throws an exception:
<blockquote>
<p>TypeError: don't know how to convert parameter 1</p>
</blockquote>
I have tried to use <code>ctypes.CFUNCTYPE(ctypes.c_char_p)</code> but that throws the same exception.
I have also tried to use <code>ctypes.CFUNCTYPE(ctypes.c_void_p)</code> but that returns a <code>NoneType</code> object.
I am able to create a <code>ctypes.c_char_p</code> object but I am not sure how to return it from the function.
I have looked at this question but the answer doesn't help me.


A:

You need to use <code>ctypes.py_object</code> as the return type and return a <code>bytes</code> object.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return b'hello'
</
