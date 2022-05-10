from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__ is Struct

# __init__ is a plain instance method
Struct.__init__ is s.__init__

# __new__ is called first
class S(Struct):
    def __new__(*args):
        print('__new__', args)
        return Struct.__new__(*args)
    def __init__(*args):
        print('__init__', args)
        return Struct.__init__(*args)
S('i')

# __new__ can return a subclass
class S(Struct):
    def __new__(*args):
        print('__new__', args)
        return type('S', (Struct,), {})
    def __init__(*args):
        print('__init__', args)
        return Struct.__init__(*args)
S('i')

# __new__ can return a subclass with a __new__
class S(Struct):
    def __new__(*args):
       
