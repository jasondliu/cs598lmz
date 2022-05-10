fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)()
fn.__code__.co_filename = fn.__code__.co_name = ''

# Test that the traceback is correct
try:
    fn()
except TypeError:
    import sys
    tb = sys.exc_info()[2]
    stack = []
    while tb:
        stack.append((tb.tb_frame.f_code.co_filename, tb.tb_lineno))
        tb = tb.tb_next
    assert stack == [('', 0), ('', 0)]
else:
    assert False, 'TypeError not raised'

# Test that the reference count is correct
import sys
fn.__code__.co_filename = fn.__code__.co_name = 'a'
gi.gi_code = fn.__code__
del fn, gi
gc.collect()
assert sys.getrefcount(sys.exc_info()[2].tb_frame.f_code) == 2
