fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: test that the __code__ attribute of a function is writable
# when the function is not a built-in function.
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #23897: test that the __code__ attribute of a built-in function is
# writable.
def g(): pass
len.__code__ = g.__code__

# Issue #23897: test that the __code__ attribute of a built-in method is
# writable.
def g(): pass
list.append.__code__ = g.__code__

# Issue #23897: test that the __code__ attribute of a method is writable.
class C:
    def m(self): pass
def g(): pass
C().m.__code__ = g.__code__

# Issue #23897: test that the __code__ attribute of a class is writable.
class C: pass
def g(): pass
C.__code__ = g.__code__


