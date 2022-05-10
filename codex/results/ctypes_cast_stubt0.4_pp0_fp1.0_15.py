import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
# Exceptions

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class UnpicklingError(Error):
    """There was a problem unpickling an object."""
    def __init__(self, args):
        self.args = args

class BadPickleGet(UnpicklingError):
    """We would need to get an object from an unpickler, but we already
    consumed the pickle."""
    pass

class BadPickleIterator(UnpicklingError):
    """We would need to get an object from an unpickler, but the
    pickle is not an iterator."""
    pass

class EmptyPickle(UnpicklingError):
    """We would need to get an object from an unpickler, but the
    pickle is empty."""
    pass

class BadPickleOperation(Error):
    """We would need to perform an operation on an unpickler, but the
    pickle is not an iterator."""
    pass


