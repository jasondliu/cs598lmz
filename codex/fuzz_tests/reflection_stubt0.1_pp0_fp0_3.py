fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator function can be called with a non-tuple argument
def gfn(x):
    yield x

gfn(1)

# Test that a generator function can be called with a tuple argument
def gfn(x):
    yield x

gfn((1,))

# Test that a generator function can be called with a tuple argument
def gfn(x):
    yield x

gfn((1, 2))

# Test that a generator function can be called with a tuple argument
def gfn(x):
    yield x

gfn((1, 2, 3))

# Test that a generator function can be called with a tuple argument
def gfn(x):
    yield x

gfn((1, 2, 3, 4))

# Test that a generator function can be called with a tuple argument
def gfn(x):
    yield x

gfn((1, 2, 3, 4, 5))

# Test that a generator function can be called with a tuple argument
def gfn(x):
    yield x


