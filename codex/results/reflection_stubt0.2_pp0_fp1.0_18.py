fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23984: Crash when __code__ is not a code object.
class A:
    def __init__(self):
        self.__code__ = None

def f():
    pass

f.__code__ = A()
f()

# Issue #23984: Crash when __code__ is not a code object.
class A:
    def __init__(self):
        self.__code__ = None

def f():
    pass

f.__code__ = A()
f()

# Issue #23984: Crash when __code__ is not a code object.
class A:
    def __init__(self):
        self.__code__ = None

def f():
    pass

f.__code__ = A()
f()

# Issue #23984: Crash when __code__ is not a code object.
class A:
    def __init__(self):
        self.__code__ = None

def f():
    pass

f.__code__ = A()

