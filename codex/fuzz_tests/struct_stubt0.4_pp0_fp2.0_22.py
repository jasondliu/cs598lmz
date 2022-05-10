from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is also called when subclassing, but the subclass instance is passed as the first argument:

class S(Struct):
    def __init__(self, *args):
        print(self)
        print(args)
        super().__init__(*args)

s = S('i')

# The __new__ method of the superclass is always called before __init__.

# The __new__ method of a metaclass is also responsible for returning an instance of the correct class.
# If the metaclass has a __prepare__ class method, it is called as the namespace for the class statement.

# A metaclass is most commonly used as a class-factory.
# The __new__ method of a metaclass is called with the name of the new class, its bases and a namespace
# containing definitions for the class body.

# The metaclass can alter the final namespace dictionary before the class is created.

# An example of a metaclass that modifies the class namespace:

class NoMixedCase
