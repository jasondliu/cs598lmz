from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__ is Struct

# __init__ is a plain instance method
Struct.__init__ is s.__init__

# __new__ is called first
class C(object):
    def __new__(cls):
        print('__new__ called')
        return super(C, cls).__new__(cls)
    def __init__(self):
        print('__init__ called')

c = C()

# __new__ can return any object
class C(object):
    def __new__(cls):
        print('__new__ called')
        return 42
    def __init__(self):
        print('__init__ called')

c = C()

# __new__ can return any object
class C(object):
    def __new__(cls):
        print('__new__ called')
        return 42
    def __init__(self):
        print('__init__ called')
