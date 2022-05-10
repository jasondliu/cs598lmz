from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__ = Struct.__dict__
class Enum(object):
    def __init__(self,y=1):
        self.x = (1,2,3)
        self.y = y

e = Enum(y=2)
e.x

e.x = (4,5,6)

