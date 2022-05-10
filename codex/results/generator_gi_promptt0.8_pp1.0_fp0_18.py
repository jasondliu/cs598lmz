gi = (i for i in ())
# Test gi.gi_code
def f():
    for i in range(10):
        if i == 2:
            yield i

gi = f()
def f():
    yield
    return

gi = f()
# Test gi.gi_frame
def f():
    yield i

# Test gi.gi_running
def f():
    while True:
        yield

gi = f()
next(gi)

# Test gi.gi_frame != NULL
def f():
    yield i

gi = f()
next(gi)

# Test gi.gi_frame == NULL
def f():
    yield i

gi = f()

# Test gi.gi_code == NULL
def f():
    return

gi = f()

# Test gi.gi_frame == NULL
def f():
    return

gi = f()
gi.gi_frame
gi.gi_frame
gi.gi_frame
gi.gi_frame
gi.gi_frame
# Test gi.gi_frame != NULL
def f():
    yield i

gi
