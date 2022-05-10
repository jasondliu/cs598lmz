import codecs
# Test codecs.register_error()

import codecs

def test(name, enc):
    print('-'*50)
    print('Encoding:', enc)
    print('Codec:', codecs.lookup(enc))
    print('String:', repr(name))
    print('Encoded:', codecs.encode(name, enc))

def register_error(encoding):
    def search_function(exc):
        print('Called:', exc)
        if not isinstance(exc, UnicodeError):
            raise TypeError("don't know how to handle %r" % exc)
        print('object:', exc.object)
        print('start:', exc.start)
        print('end:', exc.end)
        print('reason:', exc.reason)
        print('object[start:end]:', exc.object[exc.start:exc.end])
        print('encoding:', encoding)
        print('call_function:', exc.__class__.__name__)
        print('end of search_function')
        return (u'\ufffd', exc.
