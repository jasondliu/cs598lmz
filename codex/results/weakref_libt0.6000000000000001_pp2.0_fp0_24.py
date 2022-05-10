import weakref


class Singleton(type):
    """
    A metaclass that creates a Singleton base class when called.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Called when the Singleton is instantiated.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonObject(object, metaclass=Singleton):
    """
    A base class for Singleton objects.
    """
    pass


class SingletonType(type, metaclass=Singleton):
    """
    A base class for Singleton types.
    """
    pass


class WeakSingletonMetaclass(SingletonType):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__call__(*
