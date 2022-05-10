import codecs
# Test codecs.register_error

def handler(exception):
    print('handler:', exception)
    return 'xyz', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print('-'*20, encoding, '-'*20)
    try:
        u = '\u3042\u3044\u3046\u3048\u304a'
        s = u.encode(encoding, 'test.lookup')
        print(s)
    except UnicodeEncodeError as err:
        print('ERROR:', err)

for encoding in ['ascii', 'iso-8859-1', 'utf-8', 'utf-16']:
    test(encoding)

# Test codecs.register_error with a function

def handler(exception):
    print('handler:', exception)
    return 'xyz', exception.end

def test(encoding):
    print('-'*20, encoding, '-'*20)
