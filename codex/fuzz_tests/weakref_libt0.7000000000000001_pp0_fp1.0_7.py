import weakref


class Singleton(type):
    """
    Singleton metaclass
    """
    _instances = weakref.WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonError(Exception):
    pass


class SingletonInstance(object):
    """
    Singleton object
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonInstance, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class TestCase(unittest.TestCase):
    """
    Test case
    """
    def test_singleton_metaclass(self):
        class Test(metaclass=Sing
