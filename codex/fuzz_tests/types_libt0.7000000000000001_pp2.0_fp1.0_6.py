import types
types.MethodType(lambda self, x: 42, 42, int)

# A class with a __call__ method.
class Call(object):
    def __call__(self, x):
        return x + 1

# A class with __dict__, __name__ and __module__.
class Module:
    def __init__(self, name, module_dict):
        self.__dict__ = module_dict
        self.__name__ = name
        self.__module__ = name

# A class with __dict__ and __name__, but lacking __module__.
class Module2:
    def __init__(self, name, module_dict):
        self.__dict__ = module_dict
        self.__name__ = name

# A class with __dict__ and __module__, but lacking __name__.
class Module3:
    def __init__(self, name, module_dict):
        self.__dict__ = module_dict
        self.__module__ = name

# A class with __dict__, but lacking __name__ and __module__.
