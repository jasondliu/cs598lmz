import _struct
# Test _struct.Struct.__new__

# Test that _struct.Struct can be subclassed
class S(_struct.Struct):
    pass

class S2(_struct.Struct):
    def __new__(cls, *args):
        return _struct.Struct.__new__(cls, *args)

class S3(_struct.Struct):
    def __new__(cls, *args):
        return _struct.Struct.__new__(cls, *args)
    def __init__(self, *args):
        pass

class S4(_struct.Struct):
    def __new__(cls, *args):
        return _struct.Struct.__new__(cls, *args)
    def __init__(self, *args):
        raise Exception

class S5(_struct.Struct):
    def __new__(cls, *args):
        return _struct.Struct.__new__(cls, *args)
    def __init__(self, *args):
        raise Exception
    def __init_subclass__(cls, *args):

