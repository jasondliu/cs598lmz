from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__ is Struct

# __init__ is a plain instance method
Struct.__init__ is s.__init__

# __new__ is called first
class Spam:
    def __new__(cls, *args, **kwargs):
        print('Creating Instance')
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print('Initializing Instance')

s = Spam()

# __new__ is called first
class Spam:
    def __new__(cls, *args, **kwargs):
        print('Creating Instance')
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print('Initializing Instance')

s = Spam()

# __new__ is called first
class Spam:
    def __new__(cls, *args, **kw
