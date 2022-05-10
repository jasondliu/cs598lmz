fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #17077: segfault when __code__ is set to a non-code object
# with a co_code attribute
class A:
    def __init__(self):
        self.co_code = b''

def f():
    pass

f.__code__ = A()

# Issue #17077: segfault when __code__ is set to a non-code object
# with a co_code attribute
class A:
    def __init__(self):
        self.co_code = b''

def f():
    pass

f.__code__ = A()

# Issue #17077: segfault when __code__ is set to a non-code object
# with a co_code attribute
class A:
    def __init__(self):
        self.co_code = b''

def f():
    pass

f.__code__ = A()

# Issue #17077: segfault when __code__ is set to a non-code object
# with
