import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2

print s.x
print s.y

s1 = S()
s1.x = 3
s1.y = 4

print s1.x
print s1.y

s1 = s

print s1.x
print s1.y

s.x = 5
s.y = 6

print s1.x
print s1.y

s1.x = 7
s1.y = 8

print s.x
print s.y
</code>
The output is:
<code>1
2
3
4
1
2
5
6
5
6
</code>

