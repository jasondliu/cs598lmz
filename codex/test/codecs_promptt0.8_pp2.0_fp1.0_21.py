import codecs
# Test codecs.register_error() used with .read(), .readline(), .readlines()

import codecs, types

def searchfunc(encoding):
    def codec_search(e):
        if e == encoding:
            return codecs.lookup('utf-8')
        return None
    return codec_search

def enc_replace(exc):
    if not isinstance(exc, UnicodeDecodeError):
        raise TypeError('don\'t know how to handle %r' % exc)
    return (('X', exc.end),)

def read_encode_test(encoding):
    f = codecs.open('test.txt', 'r', encoding)
    s = f.read()
    if s != 'abc\n':
        raise RuntimeError
    f.close()

def readline_encode_test(encoding):
    f = codecs.open('test.txt', 'r', encoding)
    s = f.readline()
    if s != 'abc\n':
        raise RuntimeError
    f.close()

