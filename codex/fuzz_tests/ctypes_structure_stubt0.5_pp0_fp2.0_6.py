import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_float
    z = ctypes.c_char

s = S()
print s.x, s.y, s.z
s.x = 1
s.y = 2.0
s.z = 'a'
print s.x, s.y, s.z
</code>
This is what I want to do in Python.  I want to define a structure that has a variable number of members, and I want to be able to assign to those members by name.  I don't want to have to use <code>getattr</code> and <code>setattr</code>.  Is there a way to do this?
I know a class does not have to have a fixed number of members.  But I need a class that has a fixed number of members, and I need to be able to assign to them by name.  This is because I'm trying to interface with a C library where I have to pass an array of structures to a C function.  I don't know how many elements the array will have, but I do know that every element will have the same fields.
