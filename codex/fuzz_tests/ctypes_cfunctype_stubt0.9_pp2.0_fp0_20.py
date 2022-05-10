import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return int(123) # doesn't get converted to long anymore in 3.0
fun()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: 'int' object is not callable
</code>
The major difference here is that on python 2.7 <code>fun</code> is a wrapper object while on python 3 it is a <code>ctypes.CFUNCTYPE</code> object, but I'm not sure how to make it work.
How can I make Python 3 return something other than a <code>int()</code> object? What would be a good fix for this?


A:

You asked how could we make Python 3 return something other than an <code>int</code> object. That would be C code that returns a different type of object, not a <code>PyLongObject</code>.
Here's the general form of a function that returns an <code>int</code> value:
<code>PyObject *fun(PyObject *self, PyObject *args)
{
   
