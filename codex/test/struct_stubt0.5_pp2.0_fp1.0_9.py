from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Struct:
    def __init__(self, format):
        self.format = format
    def size(self):
        return struct.calcsize(self.format)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Struct:
    def __init__(self, format):
        self.format = format
    def size(self):
        return struct.calcsize(self.format)

s = Struct('i')
s.size()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Struct:
    def __init__(self, format):
        self.format = format
    def size(self):
        return struct.calcsize(self.format)
    def pack(self, *args):
        return struct.pack(self.format, *args)

s = Struct('i')
s.pack(1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Struct:
    def __init__(self, format):
        self.format = format
   
