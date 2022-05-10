fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #15: crash when printing a traceback
try:
    raise Exception
except:
    import traceback
    traceback.print_exc()

# Issue #16: crash with __class__ assignment
class A:
    pass

A.__class__ = A

# Issue #17: crash with __class__ assignment to a builtin
int.__class__ = int

# Issue #18: segfault with __class__ assignment to a builtin method
int.__add__.__class__ = int

# Issue #19: segfault with __class__ assignment to a builtin method
int.__add__.__class__ = int.__add__

# Issue #20: segfault with __class__ assignment to a builtin method
int.__add__.__class__ = int.__add__.__class__

# Issue #21: segfault with __class__ assignment to a builtin method
int.__add__.__class__ = int.__add__.__class__.__class__

#
