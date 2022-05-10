import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 4

class _Null(object):
    def __init__(self, *args, **kwargs): pass
    def __call__(self, *args, **kwargs): return _Null()
    def __getattr__(self, name): return _Null()
    def __setattr__(self, name, value): pass
    def __delattr__(self, name): pass
    def __repr__(self): return "Null()"
    def __str__(self): return "Null"
    def __len__(self): return 0
    def __getitem__(self): return _Null()
    def __setitem__(self, *args, **kwargs): pass
    def __delitem__(self, *args, **kwargs): pass
    def __iter__(self): return iter(())
    def __nonzero__(self): return False
    __hash__ = None
Null = _Null()
del _Null

# SOURCE LINE 28

class _Undefined(object):
    def
