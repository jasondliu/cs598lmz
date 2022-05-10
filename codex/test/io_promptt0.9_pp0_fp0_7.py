import io
# Test io.RawIOBase.__init__ calls

class C(io.RawIOBase): pass

def rawinit(self, f): pass
# check that we reject args
try:
    class C(io.RawIOBase):
        def __init__(self, f): rawinit(self, f)

except TypeError:
    pass
else:
    print("1. expected TypeError")

try:
    class C(io.RawIOBase):
        def __init__(self): rawinit(self)

except TypeError:
    pass
else:
    print("2. expected TypeError")

try:
    class C(io.RawIOBase):
        def __init__(self, f, s): rawinit(self, f, s)

except TypeError:
    pass
else:
    print("3. expected TypeError")


# check that we reject non-Integer return values
def change_rw(self): return "foo"

