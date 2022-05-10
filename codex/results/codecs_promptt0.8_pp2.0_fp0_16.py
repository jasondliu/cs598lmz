import codecs
# Test codecs.register_error()

import sys
# reset sys.stderr and sys.stdout to solid files
sys.stderr = open(r'test_stderr', 'w')
sys.stdout = open(r'test_stdout', 'w')

def test(enc):
    try:
        print('test encoding', enc)
        encoding = enc
        str = 'abc\u2020'
        encoded = str.encode(encoding)
        codecs.register_error(encoding, handler)
        decoded = encoded.decode(encoding)
        print('original', repr(str))
        print('encoded ', repr(encoded), 'len', len(encoded))
        print('decoded ', repr(decoded), 'len', len(decoded))
        if str == decoded:
            print('ok')
        else:
            print('decoding did not match original string')
        codecs.register_error(encoding, None)
        decoded = encoded.decode(encoding)
        print('encoded ', repr(encoded), 'len',
