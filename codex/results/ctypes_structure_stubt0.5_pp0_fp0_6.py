import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint16(1)
    y = ctypes.c_uint16(2)

s = S()

# This is the line that breaks everything
s.x = ctypes.c_uint16(2)

print(s.x)
print(s.y)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "C:\Users\J\Desktop\test.py", line 12, in &lt;module&gt;
    s.x = ctypes.c_uint16(2)
  File "C:\Program Files (x86)\Python37-32\lib\ctypes\__init__.py", line 554, in __setattr__
    self._setattr(name, value)
  File "C:\Program Files (x86)\Python37-32\lib\ctypes\__init__.py", line 566, in _setattr
    raise AttributeError(name + " is read-only")
AttributeError: x is read-only
</code>
I don't understand why
