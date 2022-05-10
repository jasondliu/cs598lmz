import gc, weakref

class SingletonClass(type):
    """
    Metaclass to implement the Singleton pattern.
    """
    def __init__(cls, name, bases, attrs):
        super(SingletonClass, cls).__init__(name, bases, attrs)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(SingletonClass, cls).__call__(*args, **kw)
        return cls.instance

class SingletonTargetCollector(object, metaclass=SingletonClass):
    """
    Singleton to collect weak references to the target objects.
    Weak references are needed to avoid memory leaks.
    """
    def __init__(self):
        self.clear()
    
    def add_target(self, target):
        """
        Add a weak reference to the target object.
        """
        self.cid = target.cid
        self.target_wr = weakref.ref(target)

