import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

first = S()
second = S()
print first.x, first.y
print second.x, second.y

second.x = 4
second.y = 5
print first.x, first.y
print second.x, second.y

S.x = ten = ctypes.c_int(10)
print first.x, first.y
print second.x, second.y
S.x = ctypes.c_int(1)
print first.x, first.y
print second.x, second.y
</code>
which gives the following output:
<code>1 2
1 2
1 2
4 5
1 2
10 2
10 2
1 2
10 2
</code>
So we see that the class attribute, <code>x</code>, is assigned to all the instances, but the class attribute, <code>y</code>, is assigned per instance. And changing the class attribute of <code>x</code> works if the new value is not a
