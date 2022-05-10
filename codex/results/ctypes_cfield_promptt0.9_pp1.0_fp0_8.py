import ctypes
# Test ctypes.CField.from_address
from ctypes import *
if sizeof(c_long) != sizeof(c_void_p):
    print("SKIP")
    raise SystemExit

libc = CDLL("libc.so.6")

printf = libc.printf
printf("Hello, %s.\n", b"CField")

w = c_wchar(65)
p = cast(byref(w), POINTER(c_wchar))
field = CField.from_address(addressof(w), p._type_, "my_wchar")
print(w.value, field.value)
w.value += 1
print(w.value, field.value)
field.value += 1
print(w.value, field.value)

# calling field() creates a *new* object
f2 = field()
assert id(f2) != id(field)
w.value += 1
print(f2.value)

p = cast(byref(w), POINTER(c_ushort))
field = CField.from_address(addressof(
