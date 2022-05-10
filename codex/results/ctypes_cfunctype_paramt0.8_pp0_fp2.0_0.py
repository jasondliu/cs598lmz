import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
func_address = 0x00002722
my_function = FUNTYPE(func_address)
my_function()
</code>
I get this error:
<code>Traceback (most recent call last):
  File "C:\python.py", line 6, in &lt;module&gt;
    my_function = FUNTYPE(func_address)
  File "C:\Python27\lib\ctypes\__init__.py", line 362, in __init__
    self._objects = []
  File "C:\Python27\lib\ctypes\__init__.py", line 363, in _objects
    self._objects.append(weakref.ref(obj))
AttributeError: 'int' object has no attribute 'append'
</code>
What am I doing wrong?


A:

The problem is that you pass <code>0x2722</code> as the prototype of your function. Per the <code>ctypes</code> documentation, this must be a Python callable:
<blockquote>
<p><code>&lt;code&gt;FUN
