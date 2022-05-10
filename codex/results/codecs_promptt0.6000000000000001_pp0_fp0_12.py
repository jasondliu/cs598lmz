import codecs
# Test codecs.register_error to replace UnicodeEncodeError
def replace_error(exception):
    print('replace_error:', exception)
    return (' ', exception.start + 1)
codecs.register_error('test.replace', replace_error)
print(s.encode('ascii', 'test.replace'))

print('-' * 20)

# Test codecs.register_error to replace UnicodeDecodeError
def ignore_error(exception):
    print('ignore_error:', exception)
    return (u'\ufffd', exception.end)
codecs.register_error('test.ignore', ignore_error)
print(b'\xc3\xb1\xc3\xb2\xc3\xb3'.decode('ascii', 'test.ignore'))
