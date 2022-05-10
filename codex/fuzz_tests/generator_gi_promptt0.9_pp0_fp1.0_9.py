gi = (i for i in ())
# Test gi.gi_code.
gi_code = gi.gi_code
for attr in ("co_argcount", "co_nlocals", "co_stacksize", "co_flags", "co_code",
             "co_consts", "co_names", "co_varnames", "co_filename",
             "co_name", "co_firstlineno", "co_lnotab"):
    descr = getattr(gi_code, 'co_' + attr)
    assert descr
    value = getattr(gi_code, attr)
    assert descr.data[gi.gi_frame.get_val_addr(gi_code) + descr.offset] == value

def f(x):
    yield x
    return 1/0

x = f(1)
y = f(2)

def g():
    yield (yield x)
    yield (yield y)
    return 1/0

h = g()
h.gi_code.co_filename = "<foo>"
h.gi_code.co_name =
