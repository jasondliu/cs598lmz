import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)
    y = ctypes.c_int(0)

S1 = S()
S2 = S()

S1.x = 1
S1.y = 2
S2.x = 3
S2.y = 4

print "S1.x", S1.x
print "S1.y", S1.y
print "S2.x", S2.x
print "S2.y", S2.y
</code>
This outputs:
S1.x 1
S1.y 2
S2.x 3
S2.y 4
Now i was expecting that this would not output the first 3 lines.  This is because i am only setting x, y on S2.  I thought that maybe this was a mistake on my part so i went and looked at the documentation.
https://docs.python.org/2/library/ctypes.html?highlight=ctypes
It states the following:
The Structure class in the ctypes module is used to create C-style Structure types. The default value for each instance attribute of a Structure is
