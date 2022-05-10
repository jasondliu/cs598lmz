import codecs
# Test codecs.register_error
import binascii

def replace_error(exc):
    import os
    if not isinstance(exc, UnicodeDecodeError):
        raise TypeError("don't know how to handle %r" % exc)
    print('replace_error:', exc.object[exc.start:exc.end])
    print('replace_error:', repr(exc.object[exc.start:exc.end]))
    print('replace_error:', binascii.hexlify(exc.object[exc.start:exc.end]))
    print('replace_error:', (binascii.hexlify(exc.object[exc.start:exc.end])).decode('ascii'))
    print('replace_error:', os.getcwd())
    print('replace_error:', exc.reason)
    # print('replace_error:', exc.object[exc.start:1])
    # print('replace_error:', exc.object[exc.start:3])
    # print('replace_error:', exc.object[exc.start:6])
