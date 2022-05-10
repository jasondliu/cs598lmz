import codecs
# Test codecs.register_error

# On error, this error handler returns the first character that could not be
# decoded, followed by the (unicode) replacement char
def errhandler(exc):
    return exc.object[exc.start:exc.end], u'?'

codecs.register_error('testcode', errhandler)

def test(name):
    print('Testing', name)
    e = codecs.getencoder(name)
    d = codecs.getdecoder(name)
    s = u'abc\xac\u1234\u20ac\u8000'
    for m in [1, 2, 3]:
        for enc in [ e, e(errors='replace'), e(errors='ignore') ]:
            x, _ = enc(s, m)
            print(x, len(x), int(x[0]))
            for dec in [ d, d(errors='replace'), d(errors='ignore'),
                         d(errors='testcode') ]:
                y, _ = dec(x, m)
                print(y)

#test('utf-7
