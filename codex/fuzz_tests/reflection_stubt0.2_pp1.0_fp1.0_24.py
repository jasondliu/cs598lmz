fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18094: crash when __code__ is not a code object
class C:
    def __init__(self):
        self.__code__ = None

def f():
    pass

f.__code__ = C()

# Issue #18095: crash when __code__ is not a code object
class C:
    def __init__(self):
        self.__code__ = None

def f():
    pass

f.__code__ = C()

# Issue #18096: crash when __code__ is not a code object
class C:
    def __init__(self):
        self.__code__ = None

def f():
    pass

f.__code__ = C()

# Issue #18097: crash when __code__ is not a code object
class C:
    def __init__(self):
        self.__code__ = None

def f():
    pass

f.__code__ = C()

# Issue #18098: crash when __code__
