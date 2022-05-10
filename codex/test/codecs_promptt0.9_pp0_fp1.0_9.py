import codecs
# Test codecs.register_error
# UTF-16 skips every other byte:

s = u'a\0b\0c\0'
u2 = codecs.utf_16_decode(s.encode('utf-16'))[0]
