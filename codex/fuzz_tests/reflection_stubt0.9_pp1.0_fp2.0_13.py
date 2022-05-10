fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__
fn.__code__ = Expression("()")

# Unsupported expressions
from types import FunctionType

def f(): pass
class C(Exception): pass

FunctionType.__code__ = Expression("()")
FunctionType.__defaults__ = Expression("()")
FunctionType.__dict__ = Expression("()")
FunctionType.__doc__ = Expression("()")
FunctionType.__closure__ = Expression("()")
FunctionType.__name__ = Expression("()")
FunctionType.__module__ = Expression("()")
FunctionType.__qualname__ = Expression("()")

C.__bases__ = Expression("()")
C.__flags__ = Expression("()")
C.__mro__ = Expression("()")
C.__subclasses__ = Expression("()")

C.__abstractmethods__ = Expression("()")
C.__base__ = Expression("()")
C.__weakrefoffset__ = Expression("()")
C.__dictoffset__ = Expression("()")

# Something to make this work under python 2
from collections import
