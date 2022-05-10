import codecs
# Test codecs.register_error('strict', strict_errors)
# Test codecs.register_error('ignore', ignore_errors)
# Test codecs.register_error('replace', replace_errors)
# Test codecs.register_error('xmlcharrefreplace', xmlcharrefreplace_errors)
# Test codecs.register_error('backslashreplace', backslashreplace_errors)
# Test codecs.register_error('namereplace', namereplace_errors)

# Test encodings module APIs

# Test getregentry()
r = codecs.getregentry('utf-8')
if r is not codecs.utf_8_encode:
    print('getregentry() wrong result for utf-8')

# Test lookup()
e = codecs.lookup('utf-8')
if e is not codecs.utf_8_encode:
    print('lookup() wrong result for utf-8')

# Test encode()
if '\xe4\xf6\xfc'.encode('utf-8') != b'\xc3\xa4\xc3\xb6\
