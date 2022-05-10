import weakref

from . import _core
from . import _util
from . import _thread

class _Event(object):
    def __init__(self):
        self.__handlers = weakref.WeakKeyDictionary()
        self.__lock = _thread.Lock()
        self.__event = _thread.Event()
        self.__count = 0

    def __iadd__(self, handler):
        with self.__lock:
            self.__handlers[handler] = None
            self.__count += 1
            self.__event.set()
        return self

    def __isub__(self, handler):
        with self.__lock:
            del self.__handlers[handler]
            self.__count -= 1
            if self.__count == 0:
                self.__event.clear()
        return self

    def __call__(self, *args, **kwargs):
        with self.__lock:
            if self.__count > 0:
                for handler in self.__handlers:
                    handler(*args, **kwargs)


