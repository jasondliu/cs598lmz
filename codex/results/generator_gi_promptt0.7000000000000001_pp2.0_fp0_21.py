gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)
# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)
# Test gi.__init__
print(gi.__init__)

def g():
    yield 1

# Test g.gi_code.co_flags
print(g.gi_code.co_flags)
# Test g.gi_frame
print(g.gi_frame)
# Test g.__init__
print(g.__init__)
