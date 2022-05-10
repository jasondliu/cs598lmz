import codecs
# Test codecs.register_error()

import codecs

def my_error(exception):
    print('my_error called with %s' % exception)
    return (u'', exception.end)

codecs.register_error('test.myerror', my_error)

def test(encoding):
    print('TEST:', encoding)
    try:
        u'\udc00'.encode(encoding)
    except UnicodeEncodeError as err:
        print('ERROR:', err)
        print('BACKTRACE:', err.__traceback__)
        print('REPR:', repr(err))
        print('STR:', str(err))
        print()

test('ascii')
test('latin-1')
