import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    a = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3
s.a = 4

print(s.x, s.y, s.z, s.a)

print(s.x.value, s.y.value, s.z.value, s.a.value)

print(s.x.__dict__)
print(s.y.__dict__)
print(s.z.__dict__)
print(s.a.__dict__)
</code>
Output:
<code>1 2 3 4
1 2 3 4
{'value': 1, '_type_': &lt;class 'ctypes.c_int'&gt;}
{'value': 2, '_type_': &lt;class 'ctypes.c_int'&gt;}
{'value': 3, '_type_': &lt;class 'ctypes.c_
