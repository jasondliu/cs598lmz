import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print(exception)
    return ('', exception.end)

codecs.register_error('test.myerror', handler)

def test(encoding):
    print(encoding, ':', end=' ')
    try:
        codecs.decode(b'\xff', encoding)
    except UnicodeDecodeError as e:
        print(e)

test('ascii')
test('iso8859-1')
test('test.myerror')

# Test that codecs.register_error() does not accept unknown error handlers

import codecs

def handler(exception):
    print(exception)
    return ('', exception.end)

codecs.register_error('test.myerror', handler)

def test(encoding):
    print(encoding, ':', end=' ')
    try:
        codecs.decode(b'\xff', encoding)
    except UnicodeDecodeError as e:
        print(e)

test('as
