import codecs
# Test codecs.register_error
def codec_error_handler(exception):
    if exception.object[exception.start] == 'X':
        return (u'Y',exception.end)
    else:
        return (u'?',exception.end+1)

codecs.register_error('test.codec',codec_error_handler)

print codecs.decode('X\x00\x00\xff','test.codec',
                    'backslashreplace')

# UnicodeError: unichr() arg not in range(0x10000) (narrow Python build)

# Test codec lookup by name
def search_function(encoding):
    if encoding == 'test.codec':
        return codecs.lookup('utf-16')
    return None

codecs.register(search_function)

print codecs.decode('\xff\xfe\x42\x00','test.codec')
print codecs.encode(u'\u1234','test.codec')

# Test builtin codec search
def search_function(enc
