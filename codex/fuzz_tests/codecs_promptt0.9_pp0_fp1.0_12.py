import codecs
# Test codecs.register_error
def strict_error_handler(error):
    print('Strict error handler:', error)
    raise UnicodeError('Replacement for codecs')
def replace_and_ignore_error_handler(error):
    print('Replace and ignore error handler:', error)
    return (u'*', error.start + 1)
with open('C:/raspi_web_english/testfile.txt', 'w') as f:  # Create a test file
    f.write('änd')
codecs.register_error('strict_error_handler', strict_error_handler) # Register error handler
codecs.register_error('replace_and_ignore_error_handler', replace_and_ignore_error_handler) # Register error handler
with codecs.open('C:/raspi_web_english/testfile.txt', 'r', encoding='latin-1', errors='strict_error_handler') as f: # This will fail with a UnicodeError
    f.read()
##with codecs.open('C:/raspi_web_english/testfile.txt
