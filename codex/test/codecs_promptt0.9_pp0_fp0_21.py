import codecs
# Test codecs.register_error and PyUnicode_AsEncodedString
# This ensures that PyUnicode_AsEncodedString sets a ValueError
# when trying to encode an unencodable character.
s = codecs.register_error('test', lambda x: (x, x))
result = []
inputs = u"A\x80B\x80CD"
for c in inputs:
    result += [ord(c)]
