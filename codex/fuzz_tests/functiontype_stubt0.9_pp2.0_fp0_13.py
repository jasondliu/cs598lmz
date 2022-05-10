from types import FunctionType
a = (x for x in [1])
b = FunctionType(a.gi_code, a.gi_frame.f_globals, a.gi_name, a.gi_frame.f_locals)
assert b.__closure__
# Old, using gen_send
assert b.__closure__ == b.__closure__


# Some tests around deep recursion with generators. We should
# raise RuntimeError if frame depth is greater than 1000.
# A frame depth of 1002 is the one where we start to get the
# recursion error (with 64 bit values on the stack it takes three
# of them to overflow)
def g():
    i = 0
    while 1:
        yield i
        i += 1


# This works ok
for i in g():
    pass

# But shouldn't work with recursion
try:

    def h(g):
        try:
            next(g)
        except StopIteration:
            pass

    h(g())
    assert 0
except RuntimeError:
    pass
