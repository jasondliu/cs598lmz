import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(isinstance(S.x, ctypes.CField)) # False

# &gt;&gt;&gt; dir(S.x)
# ['__class__', '__get__', '__new__', '__set__', '_length_', '_offset_', '_pack_', '_sizeofinstances', '_type_', '_type_', 'from_param', 'in_dll', 'in_dll_impl', 'out', 'value', 'value_g', 'value_s']
</code>
That being said, <code>S.x.__class__</code> is <code>ctypes._CData</code>, which is a subclass of <code>ctypes._SimpleCData</code>, which is a subclass of <code>ctypes.CField</code>. <code>CField</code> itself is not a subclass of <code>_CData</code>, which is why <code>isinstance(S.x, ctypes.CField)</code> is False.

