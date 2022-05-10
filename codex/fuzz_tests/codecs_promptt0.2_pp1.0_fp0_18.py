import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print('my_error_handler:', exception)
    return '', exception.end

codecs.register_error('test.myerror', my_error_handler)

def test(encoding):
    print('TEST:', encoding)
    try:
        u = '\u3042\u3044\u3046\u3048\u304a'
        s = u.encode(encoding, 'test.myerror')
        print('RETURNED:', s)
    except UnicodeError as err:
        print('ERROR:', err)

for encoding in ['iso8859-1', 'iso8859-2', 'iso8859-3', 'iso8859-4']:
    test(encoding)

# Test codecs.lookup()

import codecs

def test(encoding):
    print('TEST:', encoding)
    try:
        info = codecs.lookup(encoding)
        print('INFO:', info)

