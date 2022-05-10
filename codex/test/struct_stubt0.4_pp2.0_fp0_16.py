from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', '<')

def unpack(data):
    return s.unpack(data)[0]

def pack(data):
    return s.pack(data)

def size():
    return s.size

#===========================================================
#===========================================================

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', '>')

def unpack(data):
    return s.unpack(data)[0]

def pack(data):
    return s.pack(data)

def size():
    return s.size

#===========================================================
#===========================================================

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', '<')

def unpack(data):
    return s.unpack(data)[0]

def pack(data):
    return s.pack(data)

def size():
    return s.size

#===========================================================
#===========================================================

