fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()  # should not raise a TypeError

# Previously, the __code__ attribute of a function could be set
# to a tuple. Now, it must be a CodeType instance.
fn = lambda: None
try:
    fn.__code__ = ()
except TypeError:
    pass
else:
    raise RuntimeError("did not raise TypeError")

# It is possible to inherit from builtin types, even if they are
# "sealed" (i.e. their __setattr__ or __slots__ makes them immutable).
# The types module defines a metaclass that allows this.

import types

class MyDict(dict, metaclass=types.Sized): pass
d = MyDict()
d['a'] = 1
len(d) == 1

# It is not possible to inherit from a builtin type if it uses
# slots and defines a __new__ method, if the __new__ method of the
# subclass does not accept the same arguments as the builtin type.
# This restriction is necessary to preserve the invariant that
# the __dict__
