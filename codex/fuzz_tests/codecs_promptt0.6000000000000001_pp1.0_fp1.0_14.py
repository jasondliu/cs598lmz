import codecs
# Test codecs.register_error() and the "replace" error handler.

open = codecs.open

def test(name, encoding):
    print name, '...'
    f = open(TESTFN, 'w', encoding)
    f.write('\xff\xff\xff')
    f.close()
    f = open(TESTFN, 'r', encoding, 'replace')
    s = f.read()
    f.close()
    if s != '\ufffd\ufffd\ufffd':
        print 'encoding:', s.encode(encoding)
        print 'expected: \\xff\\xff\\xff'
        raise TestFailed, 'replace error handler did not work'

test('latin-1', 'latin-1')
test('utf-8', 'utf-8')
test('utf-16', 'utf-16')
test('utf-16-le', 'utf-16-le')
test('utf-16-be', 'utf-16-be')
test('utf-16-le', 'utf-16-le')
test('utf-16-be
