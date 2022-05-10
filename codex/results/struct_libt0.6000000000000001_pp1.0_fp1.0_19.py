import _struct

def is_little_endian():
    return (sys.byteorder == 'little')

def is_big_endian():
    return (sys.byteorder == 'big')

def reverse_bytes(data):
    '''
    Reverse a byte string, i.e. convert it from little-endian to big-endian or vice versa
    '''
    return data[::-1]

def decode_le(type, data):
    '''
    Decode a little-endian byte string into a number
    '''
    if is_big_endian():
        data = reverse_bytes(data)
    return _struct.unpack('<' + type, data)[0]

def decode_be(type, data):
    '''
    Decode a big-endian byte string into a number
    '''
    if is_little_endian():
        data = reverse_bytes(data)
    return _struct.unpack('>' + type, data)[0]

def decode_le_float(data):
    '''
   
