fn = lambda: None
gi = (i for i in ())
fn.__code__ = type(gi)
gi = fn()
gi.send(42)
gi.gi_running
gi.gi_frame.f_lasti
try:
    gi.send(42)
except TypeError:
    pass
else:
    raise Exception("Send on stopped generator should have raised TypeError")

def f():
    yield 42

gi = f()
gi.send(42)
gi.gi_running
gi.gi_frame.f_lasti + 1
try:
    gi.send(42)
except TypeError:
    pass
else:
    raise Exception("Send on stopped generator should have raised TypeError")

class G:
    def __iter__(self):
        yield 42

gi = G().__iter__()
gi.send(42)
gi.gi_frame.f_lasti
gi.gi_running
try:
    gi.send(42)
except TypeError:
    pass
else:
    raise Exception("Send on stopped generator should have raised TypeError")

# Test generator expressions

gen = (x**2 for
