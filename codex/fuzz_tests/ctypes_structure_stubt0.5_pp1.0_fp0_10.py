import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

# create a new variable for the class
s = S()

# set values
s.x = 1
s.y = 2

# print
print(s.x, s.y)

# create a pointer to the class
sp = ctypes.pointer(s)

# print the address of the pointer
print(sp)

# print the value of the pointer
print(sp.contents)

# print the value of the pointer with the value
print(sp.contents.x, sp.contents.y)

# change the values
s.x = 3
s.y = 4

# print the value of the pointer with the new value
print(sp.contents.x, sp.contents.y)

# print the value of the pointer with the new value
print(sp.contents.x, sp.contents.y)

# print the address of the pointer
print(sp)

# print the address of the pointer
print(sp)

# print the address of
