from _struct import Struct
s = Struct.__new__(Struct)

s.endianness = Struct.__dict__["_endian_"]["@"]
s.size = Struct.__dict__["_size"]
s.format = Struct.__dict__["_fmt_"]

def unpack_from(buf, offset):
    """
    Unpack the value of this data structure from the given buffer
    starting at the given offset.
    """
    ret = s.unpack_from(buf, offset)
    return ret[0]

def pack_into(buf, offset, value):
    """
    Pack the value of this data structure into the given buffer
    starting at the given offset.
    """
    s.pack_into(buf, offset, value)

if __name__ == "__main__":
    # unit test code.
    import binascii
    s = struct.Struct("I")
    values = (1,2,3,4)
    print("original:", values)

    b = bytearray(s.size * len(values))
    
    for idx, val in enumer
