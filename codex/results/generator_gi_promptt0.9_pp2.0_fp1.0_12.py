gi = (i for i in ())
# Test gi.gi_code won't segfault when gi.gi_code is NULL
gi.gi_code
gi.gi_code.gi_frame
gi.gi_code.co_name
gi.gi_code.co_filename
try:
    gi.gi_code.co_lnotab
except ValueError:
    pass
# test that we can call __repr__ on the code object
repr(gi.gi_code)
try:
    co = compile("", "", "exec")
    co.co_lnotab
except ValueError:
    pass
# test that we can call __repr__ on the NULL code object
repr(co)

s = 0
def f():
    global s
    s += 1

try:
    raise KeyError
except:
    # Just a random exception
    f()
    import sys
    tb = sys.exc_info()[2]
    # We must be in the same frame
    tb = tb.tb_next
    assert tb.tb_frame.f_code is f.__code
