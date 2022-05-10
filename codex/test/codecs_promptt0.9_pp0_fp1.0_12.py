import codecs
# Test codecs.register_error
def strict_error_handler(error):
    print('Strict error handler:', error)
    raise UnicodeError('Replacement for codecs')
def replace_and_ignore_error_handler(error):
    print('Replace and ignore error handler:', error)
    return (u'*', error.start + 1)
