import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.subtype = ctypes.c_uint16

s = S()
s.x = 0x12345

buf = ctypes.string_at(ctypes.pointer(s), ctypes.sizeof(s))

# ValueError: bad marshal data (unknown type code)
</code>
Of course, ctypes doesn't take private members into account, so you can not, for example, modify the <code>_b_needsfree_</code> members of <code>PyCArgObject</code>.  This can have unpleasant consequences when calling functions expecting pointers to arrays.  For example, if you set <code>format</code> to <code>'i'</code>, when you pass the pointer to <code>to_string</code>, you will see that there are ignored slots, like this:
<code>&gt;&gt;&gt; s = ctypes.create_string_buffer(3 * 4)
&gt;&gt;&gt; p = ctypes.pointer(s)
&gt;&gt;&gt; ptype = ctypes.PyC
