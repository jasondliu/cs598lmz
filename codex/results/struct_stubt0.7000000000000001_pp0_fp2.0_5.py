from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<h")
s.__call__(b'\x01\x00')

# ####################
def signed_to_unsigned(b):
    if b < 0:
        b = b + 256
    return b

# ####################
def unsigned_to_signed(b):
    if b > 128:
        b = b - 256
    return b

# ####################
def read_ushort(data, offset):
    return (data[offset] + data[offset + 1] * 256) % 65536

# ####################
def read_short(data, offset):
    if data[offset] > 128:
        return data[offset] - 256 + data[offset + 1] * 256
    else:
        return data[offset] + data[offset + 1] * 256

# ####################
def bytes_to_str(data, offset, length):
    return "".join([chr(c) for c in data[offset:offset + length]])

# ####################
def bytes_to_word(data
