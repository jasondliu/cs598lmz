fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #14095: Crash when calling a method of a class with a __getattr__
# defined.
class A(object):
    def __getattr__(self, attr):
        return 42
A().__hash__()

# Issue #14096: Crash when calling a method of a class with a __getattribute__
# defined.
class A(object):
    def __getattribute__(self, attr):
        return 42
A().__hash__()

# Issue #14097: Crash when calling a method of a class with a __getattr__
# defined.
class A(object):
    def __getattr__(self, attr):
        return 42
A().__repr__()

# Issue #14098: Crash when calling a method of a class with a __getattribute__
# defined.
class A(object):
    def __getattribute__(self, attr):
        return 42
A().__repr__()

# Issue #14097: Crash when calling a method of a
