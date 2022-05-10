fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #26897: test that the __code__ attribute of a built-in function
# can be set to a code object.
def f(): pass
f.__code__ = type(f).__code__
f()

# Issue #26897: test that the __code__ attribute of a built-in function
# can be set to a code object.
def f(): pass
f.__code__ = type(f).__code__
f()

# Issue #26897: test that the __code__ attribute of a built-in function
# can be set to a code object.
def f(): pass
f.__code__ = type(f).__code__
f()

# Issue #26897: test that the __code__ attribute of a built-in function
# can be set to a code object.
def f(): pass
f.__code__ = type(f).__code__
f()

# Issue #26897: test that the __code__ attribute of a built-in function
# can be set to a code object.
def
