import types
types.MethodType(lambda self: None, None, cls)

# This should not crash
class cls(object):
    def __init__(self):
        self.__class__.__init__ = lambda self: None

# This should not crash
class cls(object):
    def __init__(self):
        self.__class__.__init__ = lambda self: None
        self.__class__.__init__(self)

# This should not crash
class cls(object):
    def __init__(self):
        self.__class__.__init__ = lambda self: None
        self.__class__.__init__(self)
        self.__class__.__init__ = lambda self: None

# This should not crash
class cls(object):
    def __init__(self):
        self.__class__.__init__ = lambda self: None
        self.__class__.__init__(self)
        self.__class__.__init__ = lambda self: None
