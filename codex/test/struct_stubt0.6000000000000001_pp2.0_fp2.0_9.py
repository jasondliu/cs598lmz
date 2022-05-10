from _struct import Struct
s = Struct.__new__(Struct)
s.format = '5s'
s.size = s.calcsize(s.format)

def pack(v):
    return s.pack(v)

def unpack(v):
    return s.unpack(v)

def calcsize():
    return s.size

try:
    from _struct import pack, unpack, calcsize
except:
    pass

# ===============================================================================
#
# ===============================================================================

def make_hash(data, length=None, hashfunc=None):
    if length is None:
        length = len(data)
    if hashfunc is None:
        hashfunc = hash
    return hashfunc(data) % length

# ===============================================================================
#
# ===============================================================================

def make_hash_f(data, hashfunc=None):
    if hashfunc is None:
        hashfunc = hash
    return hashfunc(data)

# ===============================================================================
#
# ===============================================================================

