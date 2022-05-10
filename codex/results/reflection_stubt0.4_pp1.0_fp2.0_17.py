fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #12
def f():
    pass
f.__code__ = None
f()

# issue #13
def f():
    pass
f.__code__ = 1
f()

# issue #14
def f():
    pass
f.__code__ = []
f()

# issue #15
def f():
    pass
f.__code__ = {}
f()

# issue #16
def f():
    pass
f.__code__ = "foo"
f()

# issue #17
def f():
    pass
f.__code__ = True
f()

# issue #18
def f():
    pass
f.__code__ = False
f()

# issue #19
def f():
    pass
f.__code__ = object()
f()

# issue #20
def f():
    pass
f.__code__ = b"foo"
f()

# issue #21
def f():
    pass
f.__code__ = bytearray(b"foo
