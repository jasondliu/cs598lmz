import types
types.MethodType(lambda self: None, None, D)

# This should not crash
class E:
    def __init__(self):
        self.__dict__ = {}

# This should not crash
class F:
    def __init__(self):
        self.__dict__ = None

# This should not crash
class G:
    def __init__(self):
        self.__dict__ = None
    def __getattr__(self, name):
        return 42

# This should not crash
class H:
    def __init__(self):
        self.__dict__ = None
    def __getattribute__(self, name):
        return 42

# This should not crash
class I:
    def __init__(self):
        self.__dict__ = None
    def __getattr__(self, name):
        return 42
    def __getattribute__(self, name):
        return 42

# This should not crash
class J:
    def __init__(self):
        self.__dict__ = None
    def __get
