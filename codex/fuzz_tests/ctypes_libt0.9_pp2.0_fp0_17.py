import ctypes
ctypes.cast(None, ctypes.py_object)
&gt;&gt;&gt; 
</code>
Am I misundestanding something?


A:

The problem is with <code>__eq__</code>. There are two reasons:

<code>__eq__</code> is defined in this way: if <code>self</code> is <code>None</code>, then the comparison will always return <code>False</code>. So, <code>None == POINTER(py_object)</code> will always return <code>False</code>.
<code>ctypes.cast</code> returns <code>None</code> if it fails: <code>ctypes.cast(None, POINTER(py_object))</code> will always return <code>None</code>.

The solution is to use <code>__ne__</code> instead:
<code>ctypes.cast(None, POINTER(py_object)) != None
</code>
This does not work in Python 2 because there <code>__ne__</code> is not defined for <code>NoneType</
