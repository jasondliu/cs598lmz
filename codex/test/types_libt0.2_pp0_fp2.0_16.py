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
