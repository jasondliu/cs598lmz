import codecs
# Test codecs.register_error

def bad_decode(input, errors='strict'):
    raise UnicodeDecodeError('unknown', input, 0, 1, 'bad')

def bad_encode(input, errors='strict'):
    raise UnicodeEncodeError('unknown', input, 0, 1, 'bad')

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

def check(x, y):
    if x != y:
        print(`x`, `y`)

check(u'\u3042'.encode('unknown', 'test.bad_encode'), 'bad')
check(u'\u3042'.encode('unknown', 'test.bad_encode'), 'bad')
check(u'\u3042'.encode('unknown', 'test.bad_encode'), 'bad')
check(u'\u3042\u3044'.encode('unknown', 'test.bad_encode'), 'badbad')
check(u'
