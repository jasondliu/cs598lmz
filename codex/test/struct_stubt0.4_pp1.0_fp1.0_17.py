from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# Create a new class that extends Struct, and override the __new__ method to
# return an instance of the class.
class MyStruct(Struct):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

s = MyStruct.__new__(MyStruct)
s.__init__('i')
s.pack(1)

# Create a new class that extends Struct, and override the __new__ method to
# return an instance of the class.
class MyStruct(Struct):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

# Create a new instance of MyStruct.
s = MyStruct.__new__(MyStruct)
s.__init__('i')
s.pack(1)

# Create a new class that extends Struct, and override the __new__ method to
# return an instance of the class.
