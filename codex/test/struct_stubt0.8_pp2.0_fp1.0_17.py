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
