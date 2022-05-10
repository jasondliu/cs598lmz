import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

# Python 2.7
# d = {fun: 42}
# TypeError: unhashable type: 'PyCFunctionObject'
</code>
How can I make a dictionary with a key that is a Python callable function and that is hashable?


A:

You could use a <code>ctypes.PyDLL</code> object instead, which is hashable. For example, on Windows:
<code>&gt;&gt;&gt; from ctypes import *
&gt;&gt;&gt; d = PyDLL('./shared.dll')
&gt;&gt;&gt; d.my_function.argtypes = [c_int, c_char_p]
&gt;&gt;&gt; d.my_function.restype = c_int
&gt;&gt;&gt; d.my_function(42, "Hello world")
42
&gt;&gt;&gt; d.my_function in {d.my_function: 42}
True
</code>
Here <code>my_function</code
