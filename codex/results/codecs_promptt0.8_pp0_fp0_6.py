import codecs
# Test codecs.register_error
codecs.register_error('myerror', codecs.replace_errors)
def py_encode(t):
    return t.encode('hex')
def py_decode(t):
    return t.decode('hex')
codecs.register(py_encode, py_decode, name='pyhex')
# Test lookup error
codecs.lookup_error('myerror')
# Test codecs.StreamWriter
# Test case 1
streamWriter = codecs.getwriter('ascii')
w = streamWriter(sys.stdout)
w.encoder.errors = 'strict'
w.write('foo\n')
w.write('test\n')
w.encoder.errors = 'ignore'
w.write('foo\n')
w.write('test\n')
w.encoder.errors = 'replace'
w.write('foo\n')
w.write('test\n')
w.encoder.errors = 'xmlcharrefreplace'
w.write('foo\n')
w.write('test\n')
