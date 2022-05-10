import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 10
s.y = 20

print(s.x, s.y)

# ctypes.c_int.from_address(id(s)).value = 100

print(s.x, s.y)
</code>
I want to change the value of <code>x</code> to 100 in the second line of the commented code. I know that I can do it by using <code>ctypes.c_int.from_address(id(s.x)).value = 100</code>. But I want to do it with <code>ctypes.c_int.from_address(id(s)).value = 100</code>.

