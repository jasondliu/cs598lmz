import _struct

__all__ = []

for name in _struct.__all__:
    __all__.append(name)
    globals()[name] = getattr(_struct, name)

# The following code is used to support FREEZE.
#
# XXX This is a gross hack at present.  We need to use a better
# XXX mechanism in the future.

if hasattr(_struct, "_clearcache"):
    _clearcache = _struct._clearcache
else:
    try:
        from _struct import _clearcache
    except ImportError:
        pass

try:
    from _struct import __doc__
except ImportError:
    pass

# The following code is used to support SRE.

if hasattr(_struct, "Struct"):
    Struct = _struct.Struct
else:
    try:
        from _struct import Struct
    except ImportError:
        pass
