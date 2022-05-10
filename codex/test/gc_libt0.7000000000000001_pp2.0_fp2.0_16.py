import gc, weakref


def _make_weakref_key(arg):
    """Helper function to build weakref dict keys.

    The weakref library provides another function that does the same thing;
    however, this function provides backwards compatibility with Python 3.2,
    which does not include the function provided by the weakref library.

    """
    if isinstance(arg, WeakKeyDictionary):
        return _make_weakref_key(arg.data)
    return weakref.ref(arg)


class WeakKeyDictionary(object):
    """A class implementing a mutable, weak-key mapping.

    This class is a wrapper around the standard Python weakref.WeakKeyDictionary
    class. It provides an additional attribute, data, which can be used to
    easily access the underlying dictionary.

    """

    def __init__(self, init_dict=None):
        if init_dict is None:
            init_dict = {}
        self._weakref_dict = weakref.WeakKeyDictionary()
        self.data = {}
        self.update(init_dict)

