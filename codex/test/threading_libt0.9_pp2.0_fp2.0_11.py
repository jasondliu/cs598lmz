import threading
threading.local

class LocalManager:
    __slots__ = ('_local',)
    
    def __init__(self):
        class Local(threading.local):
            __slots__ = ('__local__thread_level',)
        self._local = Local()
        
    def __getattr__(self, name):
        try:
            return getattr(self._local, name)
        except AttributeError:
            value = object.__new__(self.__class__)
            setattr(self._local, name, value)
            value._local = threading.local()
            return value

class _MonkeyPatch(object):
    """Adds a staticmethod to classes that contains their absolute name."""

    def __init__(self, owner):
        self.owner = owner

    def __get__(self, obj, objtype=None):
        return self.owner


class SynchronizedBaseMeta(type):
    """
    Metaclass for synchronized classes.
    """

