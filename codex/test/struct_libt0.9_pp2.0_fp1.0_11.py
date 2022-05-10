import _struct

def read_one_float(f):
    """ read one float from a file object
        f -- file object
    """
    float_size_in_bytes = _struct.calcsize("f") # float: 32-bit
    value = f.read(float_size_in_bytes)
    return _struct.unpack("f", value)[0]

def write_one_float(f, value):
    """ write one float to a file object
        f -- file object
        value -- the value to write
    """
    float_size_in_bytes = _struct.calcsize("f") # float: 32-bit
    f.write(_struct.pack("f", value))

def load_float_array(filename):
    """ load an array of float from a file
        filename -- filename
    """
    result = []
    with open(filename, "rb") as file:
        for value in iter(partial(read_one_float, file), None):
            result.append(value)
    return result

