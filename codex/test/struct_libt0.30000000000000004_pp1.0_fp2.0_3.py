import _struct

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

def _unpack(fmt, data):
    size = _struct.calcsize(fmt)
    return _struct.unpack(fmt, data[:size]), data[size:]

def _unpack_string(data):
    size, data = _unpack("<H", data)
    return data[:size[0]], data[size[0]:]

def _unpack_strings(data):
    strings = []
    while data:
        string, data = _unpack_string(data)
        strings.append(string)
    return strings

def _unpack_pascal_string(data):
    size, data = _unpack("<B", data)
    return data[:size[0]], data[size[0]:]

def _unpack_pascal_strings(data):
    strings = []
    while data:
        string, data = _unpack_pascal_string(data)
        strings.append(string)
    return strings

