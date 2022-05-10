import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def py_fun(x):
    return x

f = FUNTYPE(py_fun)
</code>
So <code>f</code> is a ctypes function type that calls <code>py_fun</code>.
<code>&gt;&gt;&gt; f(1)
1.0
</code>
But I don't know how to do this in reverse, that is, I need to write a Python function that accepts a ctypes function and calls it. I tried
<code>def call_fun(fun):
    fun(1)
</code>
but this fails with <code>ArgumentError: argument 1: &lt;class 'TypeError'&gt;: wrong type</code>. Is this possible?


A:

If you know the function definition, the most simple way is to define the function in C, then declare the function in Python and call the function.
<code>#include &lt;stdio.h&gt;

double my_func(double input)
{
    return input;

