import _struct
# Test _struct.Struct.__new__() with a string argument.
struct = _struct.Struct('hhl')

class MyStruct(_struct.Struct):
    def __new__(cls, *args):
        return _struct.Struct.__new__(cls, *args)

class MyStruct2(_struct.Struct):
    def __new__(cls, *args):
        return _struct.Struct.__new__(cls, *args)

class MyStruct3(_struct.Struct):
    def __new__(cls, *args):
        return _struct.Struct.__new__(cls, *args)

class MyStruct4(_struct.Struct):
    def __new__(cls, *args):
        return _struct.Struct.__new__(cls, *args)

class MyStruct5(_struct.Struct):
    def __new__(cls, *args):
        return _struct.Struct.__new__(cls, *args)

class MyStruct6(_struct.Struct):
    def __new__(cls, *args):
       
