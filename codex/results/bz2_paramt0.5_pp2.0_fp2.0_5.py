from bz2 import BZ2Decompressor
BZ2Decompressor.__init__ = lambda x: None
from bz2 import BZ2File
BZ2File.__init__ = lambda x, y: None
BZ2File.close = lambda x: None
BZ2File.read = lambda x, y: None
BZ2File.readline = lambda x: None
BZ2File.seek = lambda x, y: None
BZ2File.tell = lambda x: None
BZ2File.write = lambda x, y: None
BZ2File.writelines = lambda x, y: None
from collections import Counter
Counter.__init__ = lambda x: None
Counter.__delitem__ = lambda x, y: None
Counter.__getitem__ = lambda x, y: None
Counter.__init__ = lambda x, y: None
Counter.__iter__ = lambda x: None
Counter.__len__ = lambda x: None
Counter.__missing__ = lambda x, y: None
Counter.__repr__ = lambda x: None
Counter.__setitem__ = lambda x, y, z: None
Counter.__str__ =
