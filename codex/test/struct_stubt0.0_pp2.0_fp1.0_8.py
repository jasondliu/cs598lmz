from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i').__new__(str)
except TypeError as err:
    print(err)

# __init__ is not called
try:
    s = Struct.__new__(Struct, 'i')
    s.size
except AttributeError as err:
    print(err)

# __init__ must be able to initialize the instance
try:
    Struct.__new__(Struct, 'ii').__init__('i')
except TypeError as err:
    print(err)

# __init__ does not return anything
r = Struct.__new__(Struct, 'i').__init__('i')
r is None

# __new__ is called when subclassing
class S(Struct):
    def __new__(*args):
        print('S.__new__', args)
