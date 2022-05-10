import codecs
# Test codecs.register_error() - 
# this is just to show that the codecs module' register_error() function can be used to install custom unicode error handlers
# cp1251 codec is installe here with a custom unicode error handler,
# which converts the offending byte (not convertible to unicode) to a unicode character that is a dot
# used later in this script, in the unicode() call, in the example of unicode escape sequences
def codecs_test(s):
    codecs.register_error('dot', lambda x: u".")
    # return the unicode value as a normal string in Python 2
    return s.decode('cp1251', 'dot')

# codecs.register_error('dot', lambda x: u".")
# print codecs_test(b'\xec')

