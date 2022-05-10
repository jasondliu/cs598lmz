gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame are set (they are not if gi is empty).
def foo():
    global gi
    gi = (i for i in ())
try:
    foo()
except RuntimeError as e:
    pass
else:
    print('RuntimeError not raised')

class Test: pass

# Test gi.__name__
def f():
    g = (x for x in Test())
    return g
g = f()
print(g.__name__)

# Test gi.gi_frame.f_trace is None
def f():
    g = (x for x in Test())
    return g
g = f()
print(g.gi_frame.f_trace is None)

# Test gi.gi_running
def foo():
    gi = (i for i in range(3))
    li = list(gi)
    gi = (i for i in range(3))
    try:
        next(gi)
    except StopIteration:
        print('StopIteration')
    else:
        print('
