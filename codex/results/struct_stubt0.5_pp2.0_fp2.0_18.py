from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = struct.calcsize(s.format)

def read_int(buf):
    return s.unpack_from(buf)

def read_byte(buf):
    return struct.unpack('b', buf[0:1])

def read_bool(buf):
    return struct.unpack('?', buf[0:1])

def read_str(buf):
    return buf.split('\0', 1)[0]

def read_str_fix(buf, size):
    return buf[0:size]

def read_str_fix_len(buf, size):
    return buf[0:size].split('\0', 1)[0]

def read_str_fix_len_with_len(buf, size):
    return buf[0:size].split('\0', 1)[0], size

def read_str_with_len(buf):
    size = read_int(buf)
    return buf[4:4 + size], size

def read_str_with_len
