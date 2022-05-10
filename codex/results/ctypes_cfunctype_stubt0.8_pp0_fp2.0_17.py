import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Test"
</code>
It fails with:
<code>TypeError: 'CFUNCTYPE' object is not callable
</code>
If it helps, I'm working on a portable code using Cython, so I need to call it in a way that works in both Python 3.x and Python 2.7.
How can I use a callback with a return value in Cython?


A:

As you can read here, it is not possible to return a value from a callback to a C function that is declared as returning <code>void</code>. But you can use <code>void</code> return type, and pass pointer to a variable, where the callback stores the value to return.
Passing a pointer to a variable where the callback stores the value to return is not supported by Cython. But you can pass a pointer to a <code>int</code> variable, and cast it to a pointer to a structure, which contains the value you want to return.
Below is an example of this technique. I have declared a callback that returns a pointer to a string:
<code>#include &lt;stdio.h&
