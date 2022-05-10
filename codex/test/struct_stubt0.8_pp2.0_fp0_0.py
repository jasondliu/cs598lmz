from _struct import Struct
s = Struct.__new__(Struct)
def __init__(self, *args):
    assert len(args) &gt; 0
    self.format = args[0]
    self.size = s.size
s.__init__ = __init__
