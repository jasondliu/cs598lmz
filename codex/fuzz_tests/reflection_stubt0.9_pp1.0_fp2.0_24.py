fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()
""")


# Cannot create a function from a generator with a bad freevars
def gen(x):
    assert x != "bad"
    t = (i for i in ())
    t.gi_code = (gen.__code__,)
    t.gi_frame = True
    return t

try:
    exec("fn = gen('bad')", {})
except ValueError as e:
    assert str(e) == "generator already executing"
else:
    assert False, "did not raise"

# Create a stub function around a generator object
def gen(x):
    assert x == "good"
   
