from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')

def int_to_bytes(n):
    return s.pack(n)

def bytes_to_int(b):
    return s.unpack(b)[0]

def hash_to_hex(b):
    return hexlify(b).decode('ascii')

def hex_to_hash(s):
    return unhexlify(s.encode('ascii'))

def elem_to_hex(elem):
    return hexlify(elem.export()).decode('ascii')

def hex_to_elem(hex_str):
    return Element.import_(unhexlify(hex_str.encode('ascii')))

def hash_to_elem(h):
    return Element.import_(h)

def elem_to_hash(elem):
    return elem.export()

def to_hash(x):
    if isinstance(x, bytes):
        return x
