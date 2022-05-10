import types
types.MethodType(lambda self: self.__class__.__name__, None, type)

# This is a hack to get around the fact that we can't use the
# __metaclass__ attribute on Python 2.
#
# See http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
#
# We use this to make sure that all of our classes have a `__repr__` method
# that prints out the class name.

class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super(Meta, cls).__new__(cls, name, bases, dct)
        x.__repr__ = lambda self: self.__class__.__name__
        return x

class Base(object):
    __metaclass__ = Meta

#-------------------------------------------------------------------------------
# Exceptions

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ParseError(Error):
    """Exception raised for errors while parsing.
