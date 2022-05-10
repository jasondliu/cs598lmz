import _struct

def bytes_to_int(bytes):
    """Convert bytes to an integer value.

    All bytes are converted to an integer value from left to right.
    Minimal number of bytes.
    """
    out = 0
    for b in bytes:
        out = (out << 8) + b
    return out

def int_to_bytes(val, bytes_len):
    out = bytearray(bytes_len)
    for i in range(bytes_len - 1, -1, -1):
        out[i] = val & 0xFF
        val >>= 8
    return out

def bytes_to_float(bytes):
    """Convert bytes to a float value.

    Convers a bytearray of 4 bytes to a float value.
    """
    return _struct.unpack('f', bytes)[0]

def float_to_bytes(val):
    return _struct.pack('f', val)

