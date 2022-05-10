import gc, weakref, os

__all__ = ['acquire_reference', 'acquire_reference_ex',
           'acquire_references', 'acquire_references_ex',
           'release_reference', 'release_reference_ex',
           'release_references', 'release_references_ex',
           'add_reference', 'add_references',
           'wrap_object', 'wrap_objects',
           'ObjectWrapper',
           ]

class ObjectWrapper:
    """A class that hides the fact that a Python object is being wrapped."""
    __slots__ = ('_wrapped_object', '_wrapper')

    def __init__(self, wrapped_object, wrapper):
        self._wrapped_object = wrapped_object
        self._wrapper = wrapper

    def __getattr__(self, name):
        if name == '_wrapped_object':
            raise AttributeError(name)
        return getattr(self._wrapped_object, name)

