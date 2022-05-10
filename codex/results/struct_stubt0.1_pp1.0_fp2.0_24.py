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
    def __new__(cls):
        print('__new__ called')
        return super().__new__(cls)
    def __init__(self):
        print('__init__ called')

s = Spam()

# __new__ can return a different class
class Spam:
    def __new__(cls):
        print('__new__ called')
        return super().__new__(Eggs)
    def __init__(self):
        print('__init__ called')

class Eggs:
    def __init__(self):
        print('Eggs.__init__ called')

s = Spam()

# __new__ can return an instance of the class it was called on
class Spam:
    def
