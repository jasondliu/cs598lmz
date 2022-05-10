import weakref


class GenericDiffWrapper(MutableMapping):
    """Generic wrapper for classes that don't fit well for use with diff. This
    implements a mapping that treats all attributes as keys, exposing them
    through the methods __getitem__, __contains__, __setitem__ and __delitem__


    The actual item interaction will be done by the wrapped class when possible,
    otherwise it will be delegated to the class type.

    For the changes to be picked up, the wrapper has to be on the left side of
    the diff call.

    """

    def __init__(self, obj):
        """Initialize the wrapper given an object"""
        self.__obj = obj

    @property
    def __wrapped(self):
        """Return the wrapped object. Just a shortcut for internal use."""
        return self.__obj

    def __getitem__(self, key):
        """Expose  getattr as []"""
        return getattr(self.__obj, key)

    def __setitem__(self, key, value):
        """Expose setattr as []="""

