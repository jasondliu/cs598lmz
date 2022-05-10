gi = (i for i in ())
# Test gi.gi_code in loop
def f():
    for i in gi: pass
    gi.gi_code = "123"
    for i in gi: pass
f()

def f():
    def x(): pass

class c:
    "empty"

def g(): pass

class c:
    x = (g(),)

try:
    f()
except TypeError:
    pass
else:
    assert 0
