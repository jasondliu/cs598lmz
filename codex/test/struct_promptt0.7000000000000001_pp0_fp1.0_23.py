import _struct
# Test _struct.Struct()
def unpack_struct(data, format):
    return _struct.Struct(format).unpack(data)
def pack_struct(data, format):
    return _struct.Struct(format).pack(*data)

# Test array.array()
def unpack_array(data, format):
    if format == 'i':
        a = array.array('i')
    elif format == 'f':
        a = array.array('f')
    else:
        a = array.array('d')
    a.fromstring(data)
    return a

def pack_array(a, format):
    return a.tostring()

# Test struct.unpack()
def unpack_struct_func(data, format):
    return struct.unpack(format, data)

def pack_struct_func(data, format):
    return struct.pack(format, *data)

# Test numpy.frombuffer()
