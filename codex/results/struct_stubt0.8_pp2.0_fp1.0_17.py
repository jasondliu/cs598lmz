from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack(7)

# The *new* returns an instance of the class, but it is not initialized
# in the conventional way.  When *new* is used, the __init__ method of
# the base class is bypassed.  This code could have just as easily
# written the following:

class Font(Struct):
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

font = Font('times', 10, 'black')
print font.name, font.size, font.color

# The default __init__ method of object is not called because we
# explicitly called the __new__ method.

# The combination of __new__ and __init__ is used to create objects that
# are not initialized in their natural way.  The following code is one
# example of how this can be done.

from random import randrange
class Base:
    def __init__(self):
        print 'Base initializer'
    def
