import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint(0xDEADBEEFU)
    y = ctypes.c_uint(0xBAADF00DU)

s = S()
print hex(s.x.value), hex(s.y.value)

s.y = 0xF00DBAADU
print hex(s.y.value)
</code>
This will print
<code>0xdeadbeef 0xbaadf00d
0xf00dbaad
</code>
Note that the following is of course not valid syntax:
<code>s.x = 0xDEADBEEF
</code>

