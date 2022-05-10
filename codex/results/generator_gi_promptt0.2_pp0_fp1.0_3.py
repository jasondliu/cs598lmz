gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)
# Test gi.send
print(gi.send(None))
# Test gi.throw
print(gi.throw(StopIteration))
# Test gi.close
print(gi.close())
# Test gi.__next__
print(gi.__next__())
# Test gi.__iter__
print(gi.__iter__())

# Test generator.gi_code
def f():
    yield
g = f()
print(g.gi_code)

# Test generator.gi_frame
def f():
    yield
g = f()
print(g.gi_frame)

# Test generator.gi_running
def f():
    yield
g = f()
print(g.gi_running)

# Test generator.gi_yieldfrom
def f
