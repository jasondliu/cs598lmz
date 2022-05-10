import _struct
# Test _struct.Struct

# Test that a Struct subclass can be instantiated without argument.
class MyStruct(Struct):
    pass

MyStruct()

# Test that a Struct subclass can be instantiated with an argument.
class MyStruct(Struct):
    def __init__(self, format):
        Struct.__init__(self, format)

MyStruct("i")

# Test that a Struct subclass can be instantiated with an argument.
class MyStruct(Struct):
    def __init__(self, format, size=None):
        Struct.__init__(self, format, size)

MyStruct("i")

# Test that a Struct subclass can be instantiated with an argument.
class MyStruct(Struct):
    def __init__(self, format, size=None, align=False):
        Struct.__init__(self, format, size, align)

MyStruct("i")

# Test that a Struct subclass can be instantiated with an argument.
class MyStruct(Struct):
    def __init__(self, format, size=None, align=False, mode=None):
        Struct
