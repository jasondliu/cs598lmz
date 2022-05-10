import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 4

class _Null(object):
    """
    A null object that does nothing.
    """
    def __init__(self, *args, **kwargs):
        pass
    def __call__(self, *args, **kwargs):
        return self
    def __repr__(self):
        return "Null()"
    def __nonzero__(self):
        return False
    def __getattr__(self, name):
        return self
    def __setattr__(self, name, value):
        return self
    def __delattr__(self, name):
        return self
    def __getitem__(self, key):
        return self
    def __setitem__(self, key, value):
        return self
    def __delitem__(self, key):
        return self
    def __iter__(self):
        return iter(())
    def next(self):
        raise StopIteration
    def __contains__(self, item):
        return False
   
