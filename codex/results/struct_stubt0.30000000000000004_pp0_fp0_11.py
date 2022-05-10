from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__ is s.__new__

# __init__ is a normal instance method
Struct.__init__ is s.__init__

# __new__ is a static method
class C(object):
    def __new__(cls):
        print('__new__ called')
        return super(C, cls).__new__(cls)
    def __init__(self):
        print('__init__ called')

c = C()

# __new__ is a static method
class C(object):
    def __new__(cls):
        print('__new__ called')
        return super(C, cls).__new__(cls)
    def __init__(self):
        print('__init__ called')

c = C()

# __new__ is a static method
class C(object):
    def __new__(cls):
        print('__new__ called')
        return super
