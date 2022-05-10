import _struct
# Test _struct.Struct.iter_unpack()

def pack(format, *values):
    return _struct.pack(format, *values)

def unpack(format, string):
    return _struct.unpack(format, string)

def calcsize(format):
    return _struct.calcsize(format)

def iter_unpack(format, string):
    return _struct.iter_unpack(format, string)

def check(format, string, result):
    #print(format, string, result)
    assert unpack(format, string) == result
    assert list(iter_unpack(format, string)) == [result]
    if len(result) == 1:
        result = result[0]
    size = calcsize(format)
    assert iter_unpack('{}p'.format(size), string)[0][0] == result
    # try to put the format string in a global and use it
    global globalformat
    globalformat = format
    assert unpack(globalformat, string) == result
