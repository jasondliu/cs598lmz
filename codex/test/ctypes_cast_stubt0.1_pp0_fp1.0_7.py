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

class StopIteration(Error):
    """Exception raised for unimplemented features."""
    pass

# ___________________________________________________________________________
# Iterators

class Iterator(object):
    """Abstract base class for all iterator types."""

    def next(self):
        """Return the next item from the iterator.

        When exhausted, raise StopIteration.
        """
        raise StopIteration

    def __iter__(self):
        """Return the iterator itself."""
        return self

