import codecs
# Test codecs.register_error()

import io

if __name__ == '__main__':
    def handler(exception):
        return ('', exception.end)


    codecs.register_error('test', handler)
    try:
        u = codecs.decode('abc\x80def', 'latin1', 'test')
    except UnicodeDecodeError:
        print('ERROR: decode failed')
    else:
        print(u)

    try:
        u = b'abc\x80def'.decode('latin1', 'test')
    except UnicodeDecodeError:
        print('ERROR: decode failed')
    else:
        print(u)

    try:
        u = codecs.decode('abc\x80def', 'latin1', 'strict')
    except UnicodeDecodeError:
        print('ERROR: decode failed')
    else:
        print(u)

    try:
        u = b'abc\x80def'.decode('latin1', 'strict')
    except UnicodeDecodeError:
        print('ERROR: decode failed
