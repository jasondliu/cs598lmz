import _struct

def decode_float32(b):
    return _struct.unpack('>f', b)[0]

def decode_float64(b):
    return _struct.unpack('>d', b)[0]

def encode_float32(f):
    return _struct.pack('>f', f)

def encode_float64(f):
    return _struct.pack('>d', f)
