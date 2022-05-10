import ctypes
ctypes.cast(id(1), ctypes.py_object).value

print '\n'.join('{:02x}'.format(ord(c)) for c in s)
</code>

