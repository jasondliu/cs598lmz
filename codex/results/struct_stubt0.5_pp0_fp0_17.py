from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)

# but it is not that easy to do it with the class
#Struct.__new__(Struct, '>i').pack(1)
#TypeError: __new__() takes no keyword arguments

# so we need a metaclass to do this
# metaclass is just a fancy name for class factory
# a class factory is a function that creates a class
# a metaclass is a class that creates a class
# a metaclass is a class that inherits from type
# a metaclass is a subclass of type

# so this is the metaclass
class StructMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        tag = clsobj['_fmt']
        clsobj._struct = Struct(tag)
        return clsobj

# and this is the class that uses it
class Structure(metaclass=StructMeta):
   
