fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_frame.f_code
try:
    fn()
except RuntimeError as e:
    assert str(e) == ("cannot call a generator function; use a generator "
                      "expression instead")
else:
    assert False, "expected RuntimeError"

# Test that a generator function with a non-generator function body raises
# an error when called.  This test is a bit more subtle, because the
# check for whether a generator function is callable is done in the
# generator's __init__() method.  We must construct the generator
# without calling its __init__() method.
def fn():
    pass
gi = types.GeneratorType.__new__(types.GeneratorType)
gi.gi_frame = fn.__code__.__new__(fn.__code__)
gi.gi_frame.f_code = fn.__code__
gi.gi_frame.f_back = None
gi.gi_frame.f_lasti = 0
gi.gi_frame.f_lineno = fn.__code__.co_firstlineno
gi
