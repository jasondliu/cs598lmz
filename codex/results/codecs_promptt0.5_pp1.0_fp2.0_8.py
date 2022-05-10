import codecs
# Test codecs.register_error()
#
# This test is not exhaustive.  It only tests what the rest of the code
# tests.  This test should be re-written to be more complete.

class CodecRegistryError(Exception):
    pass

def raise_exception(exc):
    raise exc

def strict_errors(exception):
    raise exception

def ignore_errors(exception):
    return (u'', exception.end)

def replace_errors(exception):
    return (u'\ufffd', exception.end)

def xmlcharrefreplace_errors(exception):
    return (u'&#%d;' % ord(exception.object[exception.end]), exception.end+1)

def backslashreplace_errors(exception):
    return (u'\\x%02x' % ord(exception.object[exception.end]), exception.end+1)

class Test_Register_Error(unittest.TestCase):
    def test_register_error(self):
        self.assertRaises(TypeError, codecs.register_
