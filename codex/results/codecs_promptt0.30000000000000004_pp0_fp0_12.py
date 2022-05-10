import codecs
# Test codecs.register_error

def handler(exception):
    return ('', exception.end)

codecs.register_error('test.ignore', handler)

def test(encoding):
    print '-'*20, encoding
    try:
        u = u'\u3042\u3044'
        s = u.encode(encoding, 'test.ignore')
        print repr(s), len(s)
    except LookupError, detail:
        print 'ERROR:', detail

for encoding in ['euc_jp', 'iso2022_jp', 'shift_jis', 'utf_8']:
    test(encoding)
