import codecs
# Test codecs.register_error(), called with 'ignore', 'replace' and 'xmlcharrefreplace';
# also tests the 'name' and 'attributes' arguments.

def test(encoding, errors='strict'):
    print encoding, errors
    c = codecs.getencoder(encoding)
    codecs.register_error(encoding, lambda e: ('&%s;' % e.object[e.start], e.end+1))
    print repr(c('abc\x80def\x80', errors)[0])

test('ascii')
test('ascii', 'ignore')
test('ascii', 'replace')
test('ascii', 'xmlcharrefreplace')
test('ascii', 'strict')
test('ascii', 'replace')
test('ascii', 'xmlcharrefreplace')
