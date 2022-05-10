import weakref
# Test weakref.ref(...) with callable instance (bug  #91).

class A(object):
    def __init__(self):
        self.strval = "a"

    def __call__(*args):
        return


r = weakref.ref(A)
inst = A()
r1 = r(inst)
r2 = r(inst)
del inst
try:
    r1()
except ReferenceError:
    pass
else:
    raise AssertionError("r1 should no longer be alive")

try:
    r2()
except ReferenceError:
    pass
else:
    raise AssertionError("r2 should no longer be alive")
