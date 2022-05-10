gi = (i for i in ())
# Test gi.gi_code.co_flags, gi.gi_frame.f_code.co_flags

def g():
    yield from ()

gi = g()

print(gi.gi_code.co_flags & 0x20)
print(gi.gi_frame.f_code.co_flags & 0x20)
