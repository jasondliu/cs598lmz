import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 5

class _Null(object):
    """A null object that does nothing."""
    def __init__(self, *args, **kwargs): pass
    def __call__(self, *args, **kwargs): return self
    def __repr__(self): return "Null()"
    def __nonzero__(self): return False
    def __getattr__(self, name): return self
    def __setattr__(self, name, value): pass
    def __delattr__(self, name): pass
    def __getitem__(self, key): return self
    def __setitem__(self, key, value): pass
    def __delitem__(self, key): pass
    def __iter__(self): return iter(())
    def __len__(self): return 0
    def __str__(self): return ""
    def __lt__(self, other): return True
    def __le__(self, other): return True
    def __eq__(self, other): return True
