import ctypes
ctypes.cast(None, ctypes.c_void_p).value

# AttributeError: 'NoneType' object has no attribute 'value'

None.__int__()

# AttributeError: 'NoneType' object has no attribute '_int__'
</code>
When debugging the compiled code I found out that the memory address of <code>None</code> is <code>0</code> (<code>0x0</code> in hexadecimal notation). That's also the reason why I suppose that <code>None</code> is not an object.

