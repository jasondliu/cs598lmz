import ctypes

class S(ctypes.Structure):
    x = ()
    y = ''

struct1 = S()
struct2 = S()

# Strictly speaking, the following line is not required, but it increases
# chances to reproduce the bug in case this file is run as a standalone
# program by making struct2 and struct1 share the same instance of
# the empty tuple.
struct2.x = struct1.x

# Add an element to struct1.x.
struct1.x += (1,)

print struct1.x
# Should print (1,), not ()

print struct2.x
# Should print (), not (1,)

print struct1.x is struct2.x
# Should print False, not True

print struct1 is struct2
# Should print False, not True
</code>
Output:
<code>(1,)
(1,)
True
True
</code>
The same problem can also be observed when replacing the <code>+</code> operator with the <code>+=</code> operator and the tuple with a string.
The problem can be reproduced with the following versions of Python:

2.7.3
