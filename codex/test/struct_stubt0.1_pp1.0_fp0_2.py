from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')
Struct.__new__(Struct, 'i').size

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i', 42)
except TypeError:
    print('TypeError')

# __new__ is not called when instantiating with keyword arguments
try:
    Struct.__new__(Struct, format='i')
except TypeError:
    print('TypeError')

# __new__ is not called when instantiating from a subclass that
# doesn't override __new__
class S(Struct):
    pass
S('i')
S('i').size

# __new__ is called when instantiating from a subclass that does
# override __new__
class S(Struct):
    def __new__(*args):
        print('S.__new__', args)
        return Struct.__new__(*args)
S('i')
