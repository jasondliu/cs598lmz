import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    name = ctypes.c_char * 4

print(S.__dict__)
s = S()
print(s.__dict__)
s.x = 1
s.y = 2
s.name = b'abc'
print(s.x, s.y, s.name)
</code>
Output:
<code>{'_fields_': [('x', &lt;class 'ctypes.c_int'&gt;), ('y', &lt;class 'ctypes.c_int'&gt;), ('name', &lt;class 'ctypes.c_char_Array_4'&gt;)], '_pack_': 1, '_align': None, '_anonymous_': {}}
{}
1 2 b'abc'
</code>

