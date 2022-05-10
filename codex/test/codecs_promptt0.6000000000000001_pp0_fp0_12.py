import codecs
# Test codecs.register_error to replace UnicodeEncodeError
def replace_error(exception):
    print('replace_error:', exception)
    return (' ', exception.start + 1)
codecs.register_error('test.replace', replace_error)
