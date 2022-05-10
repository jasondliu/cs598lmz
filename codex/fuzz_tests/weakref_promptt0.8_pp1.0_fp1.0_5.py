import weakref
# Test weakref.ref() on classes, functions, modules and weakrefables
# (objects defining __weakref__)
import weakref

class C:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def method(self):
        return self

c = C('c')
d = C('d')
f = c.method

C_ref = weakref.ref(C)
c_ref = weakref.ref(c)
d_ref = weakref.ref(d)
f_ref = weakref.ref(f)

# Make sure comparing refs to objects works
if C_ref == C and C_ref is not C:
    raise TestFailed('C_ref unexpectedly identical to C')
if not (C_ref == C() and C_ref is not C()):
    raise TestFailed('C_ref unexpectedly not equal to C()')
if not (c_ref == c and c_ref is not c):
    raise TestFailed('c_ref unexpectedly not equal to c')
