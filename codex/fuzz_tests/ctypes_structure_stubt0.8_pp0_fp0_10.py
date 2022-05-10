import ctypes

class S(ctypes.Structure):
    x = 1

s = S()

# This line is the source of the memory error
ctypes.pointer(s)

del s
</code>
I faithfully documented my findings in the source code, but I don't really know how to interpret them.
I noticed that a pointer's contents are not necessarily changed to <code>NULL</code> when the object it was pointing to is destroyed.
Especially, this is the case if I store the pointer in a container, such as in a list.
<code>import ctypes

class S(ctypes.Structure):
    x = 1

s = S()
p = ctypes.pointer(s)

print(p.contents) # Prints a valid S object.

del s

print(p) # Prints a valid pointer, not NULL
print(p.contents) # Prints None

print(1 in [p]) # Prints True, the pointer is stored
del p
print(1 in [p]) # Prints False, the pointer is deleted
</code>
It seems that, because the pointer is stored, it does not become NULL,
