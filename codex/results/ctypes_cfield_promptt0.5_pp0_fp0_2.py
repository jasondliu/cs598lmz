import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
	_fields_ = [("x", ctypes.c_int),
		("y", ctypes.c_int)]

class RECT(ctypes.Structure):
	_fields_ = [("a", POINT),
		("b", POINT)]

rect = RECT((1,2), (3,4))
print(rect.a.x)
print(rect.b.y)

print("======================================")

# Test ctypes.Structure
class Test(ctypes.Structure):
	_fields_ = [("x", ctypes.c_int),
		("y", ctypes.c_int)]

t = Test()
t.x = 1
t.y = 2
print(t.x)
print(t.y)

print("======================================")

# Test ctypes.c_char_p
# ctypes.c_char_p(b"hello")
# ctypes.c_char_p("hello")

# Test ctypes.c_int
print
