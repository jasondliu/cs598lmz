fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

class A:
    def __init__(self):
        self.x = 42

# This is a test for a bug in the code generator for the
# BUILD_SLICE opcode.  The bug was that the code generator
# was using the wrong variable as the upper bound of the
# slice.  This code should print "42".
a = A()
print a.x[0:1].x

# Test for a bug in the code generator for the
# UNPACK_SEQUENCE opcode.  This code should print "42".
a, = [a]
print a.x

# Test for a bug in the code generator for the
# UNPACK_SEQUENCE opcode.  This code should print "42".
[a] = [a]
print a.x

# Test for a bug in the code generator for the
# UNPACK_SEQUENCE opcode.  This code should print "42".
a, b = a, a
print a.x

# Test for a bug in the code generator for the
# UNP
