import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField._name = 'CField'

print(type(S.x))  # &lt;class 'Field'&gt;
print(S.x)        # c_int
print(S.x == 'x') # True
</code>
If you have several types with different <code>_fields_</code> and want to compare them then you need to check that their type is <code>CField</code> and that their <code>field</code> attribute is the same:
<code>s1 = S()
s2 = S()
s1.x = 1
s2.y = 2
print(s1.x == 'x') # True
print(s1.x == 'y') # False
print(s2.y == 'x') # False
print(s2.y == 'y') # True
</code>

