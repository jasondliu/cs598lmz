import weakref

class Singleton(object):
    """
    Singleton pattern as a base class
    """
    _instances = {}
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = object.__new__(cls)
            cls._instances[cls] = weakref.proxy(instance)
        return cls._instances[cls]
