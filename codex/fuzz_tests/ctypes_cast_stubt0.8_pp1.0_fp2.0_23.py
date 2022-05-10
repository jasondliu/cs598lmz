import ctypes
ctypes.cast(p, ctypes.py_object).value

# Output: 'Hello'

# Memory address of variable
hex(id(p))
# Output: '0x23c7768'
</code>

Note that <code>id</code> is used just for displaying the address of variable in an easy way. You can also use <code>ctypes.addressof</code> to get address of variable:
<code>import ctypes
ctypes.addressof(p)

# Output: 138804960
</code>

