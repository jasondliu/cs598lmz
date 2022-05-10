import _struct

def get_int(data, offset):
    return int(data[offset:offset+4].encode('hex'), 16)

def get_float(data, offset):
    return _struct.unpack('f', data[offset:offset+4])[0]

def get_str(data, offset):
    s = ''
    while data[offset] != '\x00':
        s += data[offset]
        offset += 1
    return s

def get_vec(data, offset):
    return (get_float(data, offset), get_float(data, offset+4), get_float(data, offset+8))

def get_color(data, offset):
    return (get_float(data, offset), get_float(data, offset+4), get_float(data, offset+8), get_float(data, offset+12))

def get_quat(data, offset):
    return (get_float(data, offset), get_float(data, offset+4), get_float(data, offset+8), get_float(data
