import ctypes
ctypes.string_at(3)
</code>
This gives me the following error:
<code>TypeError: 'int' object is not callable
</code>
On the other hand, it works fine with <code>ctypes.addressof</code>.
Example:
<code>import ctypes
ctypes.addressof(1)
</code>
returns <code>140718773729472</code> as expected.
What is the reason for this?


A:

The addressof function takes a ctypes object, not just any Python object.
<code>from ctypes import *
pythonapi.PyString_AsString.restype = c_char_p
pythonapi.PyString_AsString.argtypes = [py_object]
addr = pythonapi.PyString_AsString("hello")
print ctypes.addressof(addr)
addr = pythonapi.PyString_AsString.restype(42)
print ctypes.addressof(addr)
</code>

