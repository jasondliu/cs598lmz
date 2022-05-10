import _struct
# Test _struct.Struct
sfmt = ('h', 'i', 'l', 'f', 'd', 's')
sfmt2 = ('H', 'I', 'L', 'd', 's')

def sfmtget(fmt, arr):
    if fmt == 's':
        return b''.join(map(lambda x: bytes((x,)), arr))
    return arr

def sfmtchk(fmt, arr, res):
    if fmt == 's':
        if sys.version_info < (3, 0):
            res = b''.join(map(lambda x: bytes((x,)), res))
        for i, x in enumerate(res):
            if x != arr[i]:
                raise ValueError('bad result for %s: %r != %r' % (fmt, x, arr[i]))
    else:
        for i, x in enumerate(res):
            if x != arr[i]:
                raise ValueError('bad result for %s: %r != %r' % (fmt, x, arr[i]))

def selft
