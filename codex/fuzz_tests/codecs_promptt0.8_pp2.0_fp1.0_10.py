import codecs
# Test codecs.register_error() for the "backslashreplace" error handler
# by registering it as the default error handler.

try:
    codecs.register_error('test.backslashreplace', codecs.backslashreplace_errors)
except:
    pass

# After this, all decoding and encoding errors should raise a
# UnicodeError with the bacsklashreplace encoding.

# Test the "ignore" error handler
try:
    codecs.register_error('test.ignore', codecs.ignore_errors)
except:
    pass

# After this, all decoding and encoding errors should raise a
# UnicodeError with the bacsklashreplace encoding.

# Test the "xmlcharrefreplace" error handler
try:
    codecs.register_error('test.xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
except:
    pass

# After this, all decoding and encoding errors should raise a
# UnicodeError with the xmlcharrefreplace encoding.

# Test backslashreplace error handler

TESTDECODEERRORS = [
    ('ascii', '\xc
