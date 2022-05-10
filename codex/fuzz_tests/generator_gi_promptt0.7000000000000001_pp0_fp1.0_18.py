gi = (i for i in ())
# Test gi.gi_code (code object)
print(gi.gi_code)

def gen():
    yield 1
    yield 2
    yield 3

print(gen().gi_code is gen.__code__)

# Test gi.gi_frame (frame object)
def gen2(x):
    yield x
    yield x * 2
    yield x * 3

g = gen2(5)

print(g.gi_frame.f_lasti)

# Test gi.gi_running (bool)
print(g.gi_running)
print(next(g))
print(g.gi_running)

# Test gi.gi_yieldfrom
def gen3():
    yield from range(3)

g = gen3()
print(g.gi_yieldfrom)

# Test gi.gi_frame.f_locals
def gen4(x):
    y = x * 2
    yield y

g = gen4(5)
print(g.gi_frame.f_locals)

# Test gi.gi_frame.
