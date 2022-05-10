fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the __code__ attribute can be set to a callable object
def f(): pass
def g(): pass
f.__code__ = g
f()

# Test that the __code__ attribute can be set to a callable object
# that returns a callable object
def f(): pass
def g(): pass
def h(): pass
f.__code__ = lambda: g
g.__code__ = h
f()

# Test that the __code__ attribute can be set to a callable object
# that returns a callable object that returns a callable object
def f(): pass
def g(): pass
def h(): pass
def i(): pass
f.__code__ = lambda: g
g.__code__ = lambda: h
h.__code__ = i
f()

# Test that the __code__ attribute can be set to a callable object
# that returns a callable object that returns a callable object
# that returns a callable object
def f(): pass
def g(): pass
def h(): pass
def i(): pass
def j(): pass

