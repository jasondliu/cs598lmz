import codecs
# Test codecs.register_error, even in the presence of an exception
# handler.
import encodings
import sys

encoding = 'utf-8'

def test(text, errorhandler):
    print "    " + repr(text)

    # Test the default error handler.
    try:
        s = text.encode(encoding)
        raise RuntimeError, "this should not have succeeded"
    except UnicodeEncodeError:
        pass

    # Test the given error handler.
    s = text.encode(encoding, errorhandler)
    print "        " + repr(s)
    u = s.decode(encoding, errorhandler)
    if u != text:
        raise RuntimeError, "roundtrip failed"

    # Test using codecs.register_error.
    encodings.register_error(encoding, errorhandler)
    try:
        s = text.encode(encoding)
        print "        " + repr(s)
        u = s.decode(encoding)
        if u != text:
            raise RuntimeError, "roundtrip failed"
   
