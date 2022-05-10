import ctypes
ctypes.cast(c_void_p(addr), ctypes.py_object).value
</code>

On Windows, the address of <code>obj</code> is <code>0x00A3ACE8</code> (in this case).
So you can get <code>obj</code> from <code>0x00A3ACE8</code> as follows:
<code>id(obj) == 0x00A3ACE8
</code>

