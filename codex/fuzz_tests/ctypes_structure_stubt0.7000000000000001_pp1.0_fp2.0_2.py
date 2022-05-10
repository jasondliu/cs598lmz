import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class D(ctypes.Structure):
    a = ctypes.c_int
    b = ctypes.c_int

def print_struct(struct):
    print(struct.a, struct.b)

# this doesn't work
#print_struct(S)

# but this does!
print_struct(D)
</code>
I've also tried to cast <code>S</code> to <code>ctypes.Structure</code> and that didn't work either.
Here is the error I get:
<code>Traceback (most recent call last):
  File "struct_test.py", line 18, in &lt;module&gt;
    print_struct(S)
  File "struct_test.py", line 13, in print_struct
    print(struct.a, struct.b)
AttributeError: 'type' object has no attribute 'a'
</code>


A:

<code>S</code> is a type, and those don't have attributes.
