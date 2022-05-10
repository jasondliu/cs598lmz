import ctypes
# Test ctypes.CField
# create a string
s = "Hello world"
# get the address of the first character
addr = ctypes.addressof(ctypes.c_char.from_address(id(s)).value)
print(addr)
# get the string from the address
t = ctypes.c_char_p.from_address(addr)
print(t.value.decode())
print(t.value)

# create a string
s = "Hello world"
# get a pointer to the first character
t = ctypes.pointer(ctypes.c_char.from_address(id(s)))
print(t)
# get the address
addr = ctypes.addressof(t.contents)
print(addr)
# get the string from the address
t = ctypes.c_char_p.from_address(addr)
print(t.value.decode())
print(t.value)

# create a string
s = "Hello world"
# get a pointer to the first character
t = ctypes.pointer(ctypes.c_char.from_address(id
