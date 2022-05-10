fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test __code__ on a builtin
def f(): pass
f.__code__ = lambda: None
f()

# Test __code__ on a builtin, but with a bad value
def f(): pass
f.__code__ = (i for i in ())
f()

# Test __code__ on a function
def f(): pass
f.__code__ = f
f()

# Test __code__ on a function, but with a bad value
def f(): pass
f.__code__ = lambda: None
f()

# Test __code__ on a function, but with a bad value
def f(): pass
f.__code__ = (i for i in ())
f()

# Test __code__ on a method
class C:
    def f(self): pass
C.f.__code__ = C.f
C().f()

# Test __code__ on a method, but with a bad value
class C:
    def f(self): pass
C.f.__code__ = lambda: None
C().f()


