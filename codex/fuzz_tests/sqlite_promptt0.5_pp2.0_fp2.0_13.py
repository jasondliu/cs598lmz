import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

# http://stackoverflow.com/questions/2912231/is-there-a-way-to-have-a-static-member-in-python
class _MetaSingleton(type):
    """
    A metaclass that creates a Singleton base class when called.
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(_MetaSingleton('SingletonMeta', (object,), {})):
    pass

class SharedMemory(Singleton):
    """
    A shared memory implementation for Python.
    """

    # The default size of the shared memory block.
    DEFAULT_SIZE = 4096

    # The default name of the shared memory block.
    DEFAULT_NAME = "SharedMemory"

    #
