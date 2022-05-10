from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__

# TypeError: required argument 'format' (pos 1) not found

Struct.__new__(Struct, format)

# TypeError: __new__() missing 1 required positional argument: 'self'

# The Struct.__new__() method doesn't know what to do with the
# format.
# The simplest solution is to pass the format to the cls argument
# using a lambda expression:

s = Struct.__new__(Struct, lambda: "i")
s.__dict__

# {'format': 'i'}

s = Struct.__new__(Struct, lambda: "f")
s.__dict__

# {'format': 'f'}

# However, the Struct standard constructor does something more
# and it also calls the Struct.format() method.
# So, to do the same thing we need to provide a format method

class Struct:
    @classmethod
    def format(cls, format):
        pass


class Struct:
    @classmethod
    def format(cls, format):
        cls
