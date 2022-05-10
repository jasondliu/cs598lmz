import types
types.ModuleType

from types import ModuleType

# A class for different kinds of internal objects.

class W_Root(object):
    """The base class for PyPy's internal objects.
    This is a direct subclass of `object`; most internal
    objects inherit from the more specialized `W_Object`."""

    # a cache for the type of the object, if it has any
    _type = None
    def getclass(self, space):
        """Get the type of the object.
        Most internal objects have a type, but some don't,
        like `W_NullImplementation`.  Every `W_Root` sublcass
        should have a docstring explaining whether it has a
        type or not.
        """
        if self._type is None:
            self._type = space.gettypefor(self.__class__)
        return self._type

    def str_w(self, space):
        return space.wrap(self.str(space))

