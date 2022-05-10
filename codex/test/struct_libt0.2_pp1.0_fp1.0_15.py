import _struct

def get_int(data, offset):
    return _struct.unpack_from('<I', data, offset)[0]

def get_short(data, offset):
    return _struct.unpack_from('<H', data, offset)[0]

def get_byte(data, offset):
    return _struct.unpack_from('<B', data, offset)[0]

def get_string(data, offset):
    length = get_byte(data, offset)
    offset += 1
    return (data[offset:offset+length], offset+length)

def get_bytes(data, offset, length):
    return (data[offset:offset+length], offset+length)

def get_int_array(data, offset, count):
    result = []
    for i in range(count):
        result.append(get_int(data, offset))
        offset += 4
    return (result, offset)

def get_short_array(data, offset, count):
    result = []
