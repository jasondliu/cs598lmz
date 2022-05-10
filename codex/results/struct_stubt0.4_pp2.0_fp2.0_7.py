from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__
# __init__
# __call__

class Struct:
    def __init__(self, format):
        self.format = format
    def __call__(self, *args):
        return self.format.pack(*args)
s = Struct('i')
s.size

# __new__
# __init__
# __call__

class Struct:
    def __init__(self, format):
        self.format = format
    def __call__(self, *args):
        return self.format.pack(*args)
    def size(self):
        return self.format.size
s = Struct('i')
s.size

# __new__
# __init__
# __call__

class Struct:
    def __init__(self, format):
        self.format = format
    def __call__(self, *args):
        return self.format.pack(*args)
    def size(self):
        return self.format.size
s = Struct
