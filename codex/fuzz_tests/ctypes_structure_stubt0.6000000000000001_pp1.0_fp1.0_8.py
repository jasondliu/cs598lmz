import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    y = ctypes.c_int
    z = ctypes.c_char


s = S()

s.x = 'a'
s.y = 1
s.z = 'b'

print(s.x, s.y, s.z)

# a 1 b

s = S(x='a', y=1, z='b')

print(s.x, s.y, s.z)

# a 1 b

print(s)

# &lt;__main__.S object at 0x7f6e5fb5f5e0&gt;

print(s.__dict__)

# {}

print(s._fields_)

# [('x', c_char), ('y', c_int), ('z', c_char)]

print(s.__dict__ is None)

# True
</code>
<code>ctypes</code> structures do not have a <code>__dict__</code> attribute. The <code>_fields_</code>
