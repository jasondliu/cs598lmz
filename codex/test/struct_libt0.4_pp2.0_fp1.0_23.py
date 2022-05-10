import _struct

def get_int(data, offset):
    return _struct.unpack('<I', data[offset:offset+4])[0]

def get_short(data, offset):
    return _struct.unpack('<H', data[offset:offset+2])[0]

def get_byte(data, offset):
    return _struct.unpack('<B', data[offset:offset+1])[0]

def get_string(data, offset):
    length = get_int(data, offset)
    offset += 4
    return data[offset:offset+length]

def get_bytes(data, offset, length):
    return data[offset:offset+length]

def get_bool(data, offset):
    return get_byte(data, offset) != 0

def get_int_array(data, offset):
    length = get_int(data, offset)
    offset += 4
    return [get_int(data, offset+i*4) for i in range(length)]

