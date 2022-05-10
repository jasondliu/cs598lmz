import codecs
# Test codecs.register_error and PyUnicode_AsEncodedString
# This ensures that PyUnicode_AsEncodedString sets a ValueError
# when trying to encode an unencodable character.
s = codecs.register_error('test', lambda x: (x, x))
result = []
inputs = u"A\x80B\x80CD"
for c in inputs:
    result += [ord(c)]
    encoded = c.encode('ascii', 'test')
    if encoded == '\x80':
        raise RuntimeError, 'encoded should not be the value \'\x80\''
    result += [int(encoded[0])]
    result += [int(encoded[1])]
if result != [65, 128, 65, 65, 66, 128, 66, 66, 67, 68]:
    raise RuntimeError, "result is wrong - %s" % result

try:
    u"A\x80".encode('ascii', 'test')
except UnicodeError, e:
    if e.reason != 'test: encoding failed':
        raise
