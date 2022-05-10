import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

a = S()
a.x = 1
a.y = 2
a.z = 3

b = S()
b.x = 4
b.y = 5
b.z = 6

print a.x
print a.y
print a.z

print b.x
print b.y
print b.z

c = a

print c.x
print c.y
print c.z

a.x = 7
a.y = 8
a.z = 9

print a.x
print a.y
print a.z

print b.x
print b.y
print b.z

print c.x
print c.y
print c.z
</code>
Output:
<code>1
2
3
4
5
6
1
2
3
7
8
9
4
5
6
7
8
9
</code>

