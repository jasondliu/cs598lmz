from _struct import Struct
s = Struct.__new__(Struct)
s.format = "I"
s.size = Struct.calcsize(s, s.format)
s.pack = s.__call__(s, s.format)
s.unpack = lambda b: Struct.unpack(s, s.format, b)

def host_byte_order() -> bool:
    return struct.pack("=H", 5) == struct.pack("@H", 5)

def u32_to_bytes(x):
    return struct.pack("<I", x)

def bytes_to_u32(b):
    return struct.unpack("<I", b)[0]

def u32_to_bytes_be(x):
    return struct.pack(">I", x)

def bytes_be_to_u32(b):
    return struct.unpack(">I", b)[0]

def u64_to_bytes(x):
    return struct.pack("<Q", x)

def bytes_to_u64(b):
    return struct.unpack("<Q", b)[0]
