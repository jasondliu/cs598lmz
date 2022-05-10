import gc, weakref
import inspect
import sys

if sys.version_info[0] == 2:
    import cPickle as pickle
else:
    import pickle


def _is_weakref_proxy(obj):
    return isinstance(obj, weakref.ProxyTypes)


class Unpickler(pickle.Unpickler):
    """
    An Unpickler which calls a custom constructor function for
    instances of unpickled classes, with the pickled data as an
    argument.
    """

    def __init__(self, *args, **kwargs):
        self._constructor = kwargs.pop('constructor', None)
        super(Unpickler, self).__init__(*args, **kwargs)
        self.dispatch[pickle.REDUCE] = self._constructor_setstate

    def _constructor_setstate(self, obj):
        if self._constructor:
            return self._constructor(self, obj)
        else:
            return obj


def _is_picklable(object):
    """
    Return True if
