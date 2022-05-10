import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
# Exceptions

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class NotImplementedError(Error):
    """Exception raised for unimplemented features."""
    pass

class RuntimeError(Error):
    """Exception raised for unimplemented features."""
    pass

class TypeError(Error):
    """Exception raised for unimplemented features."""
    pass

class ValueError(Error):
    """Exception raised for unimplemented features."""
    pass

# ___________________________________________________________________________
# Iterators

class Iterator(object):
    """Abstract base class for all iterator types."""

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration

# ___________________________________________________________________________
# Generators

class Generator(Iterator):
    """Abstract base class for all generator types."""

    def close(self):
        raise RuntimeError("generator ignored GeneratorExit")

    def next(self):
        raise RuntimeError
