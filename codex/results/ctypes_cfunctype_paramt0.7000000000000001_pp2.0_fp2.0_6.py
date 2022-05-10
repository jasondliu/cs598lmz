import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def function(i):
    print "Hello World: %d" % i

c_function = FUNTYPE(function)

print "Calling python function:"
function(10)

print "Calling C function:"
c_function(10)
</code>
I get the following error.
<code>Traceback (most recent call last):
  File "callbacks.py", line 13, in &lt;module&gt;
    c_function(10)
ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: Don't know how to convert parameter 1
</code>
I'd like to be able to use these ctypes C functions as callbacks in C/C++ code.


A:

You should use python api to write a wrapper for your code.
<code>#include &lt;Python.h&gt;

void call_python_function(int i)
{
    PyObject *pyfunc, *args, *result;

    pyfunc = PyDict_Get
