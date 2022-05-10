gi = (i for i in ())
# Test gi.gi_code.co_func is available, despite not being documented
assert gi.gi_code.co_func is gi.__next__


for name in dir(gi):
    if name.startswith("gi_"):
        assert name in GENERATOR_INFO_FIELDS


def check(name):
    attr = getattr(gi, name, None)
    if attr is not None:
        # some attributes are only available in CPython
        assert type(attr) == GENERATOR_FUNC.__code__.co_varnames[getattr(inspect, "CO_"+name.upper())]

check("frame")
check("running")
check("code")


# Regression for issue #17227
assert ((i for i in range(10)).gi_frame is None)
# ... unless the frame is being held alive.
def f():
    g = (i for i in range(10))
    assert g.gi_frame is not None
    return g
f().gi_frame
