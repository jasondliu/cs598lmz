import codecs
# Test codecs.register_error
a = codecs.getencoder('hex')('abc')
def hex_replace(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u'', exc.end)
codecs.register_error('my.hex', hex_replace)
b = codecs.encode('abc', 'hex', 'my.hex')

# Test codecs.lookup_error
def hex_replace2(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'', exc.end)
codecs.register_error('my.hex2', hex_replace2)
c = codecs.lookup_error('my.hex2')
d = c(UnicodeDecodeError('hex', b'1234', 3, 4, 'ouch'))

# Test codecs.strict_errors
def hex_strict(exc):
    raise TypeError
codecs.register_error('my.hex3', hex_strict)
e = codecs.strict_errors('my.hex3')
f = e(
