import codecs
# Test codecs.register_error()
def cb(error):
    print "callback called:", error
codecs.register_error('test.error', cb)
# It should not be possible to overwrite the name of an existing
# error handler.
try:
    codecs.register_error('xmlcharrefreplace', cb)
except ValueError:
    pass
else:
    raise RuntimeError, "overwrite succeeded"
# Check that the callback is indeed called
encoding = 'test.test'
codecs.register_error(encoding, cb)
print 'codecs.decode(s, "%s", "test.error")' % encoding
try:
    codecs.decode('x', encoding, 'test.error')
except UnicodeError, exc:
    print "UnicodeError:", exc
print 'codecs.decode(s, "%s", "strict")' % encoding
try:
    codecs.decode('x', encoding, 'strict')
except UnicodeError, exc:
    print "UnicodeError:", exc
# Check that the callback is indeed
