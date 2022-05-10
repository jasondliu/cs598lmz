import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p

s = S()
s.x = "abc"
print s.x
s.x = "def"
print s.x
s.x = "ghi"
print s.x
s.x = "jkl"
print s.x
s.x = "mno"
print s.x
s.x = "pqr"
print s.x
s.x = "stu"
print s.x
s.x = "vwx"
print s.x
s.x = "yz"
print s.x
</code>
Output:
<code>abc
def
ghi
jkl
mno
pqr
stu
vwx
yz
</code>

