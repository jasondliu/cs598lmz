import codecs
# Test codecs.register_error
# Test unicode
# UnicodeEncodeError: 'ascii' codec can't encode character u'\xae' in position 8: ordinal not in range(128)

# s = u'caf\xe9'
# # caf\xe9
# ss = 'caf\xE9'
# print s
# ss = s.encode('ascii', 'replace')
# ss = s.encode('ascii', 'xmlcharrefreplace')
# ss = s.encode('ascii', 'ignore')
# ss = s.encode('ascii')

# print ss

# Test unicode
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 3: ordinal not in range(128)

# s = '\xab\u2122\xbb' # non-ASCII characters

# print s
# s = s.encode('ascii')
# print s
# s = s.decode('ascii') # UnicodeDecodeError: 'ascii' codec can't
