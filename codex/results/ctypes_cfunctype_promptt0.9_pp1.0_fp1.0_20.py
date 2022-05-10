import ctypes
# Test ctypes.CFUNCTYPE.

def report(prefix, object, expected):
    print(prefix + ':', end=' ')
    try:
        result = ctypes.sizeof(object)
    except Exception as e:
        print(e)
    else:
        if result != expected:
            print('Unexpected result: %d (expected %d)...' % (result, expected), end=' ')
        else:
            print('OK', end=' ')
        print(type(object))

# Simple types.
report('None', None, 0)
report('int', 42, 4)
report('float', 3.14, 8)
report('bool', True, 1)
report('complex', 1+1j, 16)
report('string', 'Hello', 6)
report('bytes', b'Hello', 6)

# Collections (bytes and bytearray are sequences, so they are tested there).
report('tuple', (1, 2, 3), 12)
report('list', [1, 2, 3], 12)
report('set', {1, 2, 3}, 12)
report
