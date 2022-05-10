import codecs
# Test codecs.register_error()

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Testing the register_error() function
        def ignore_error(message):
            return (u"", message.start + 1)
        codecs.register_error("ignore", ignore_error)
        codecs.register_error("replace", codecs.replace_errors)
        codecs.register_error("xmlcharrefreplace", codecs.xmlcharrefreplace_errors)
        codecs.register_error("backslashreplace", codecs.backslashreplace_errors)
        codecs.register_error("strict", codecs.strict_errors)
        codecs.register_error("surrogateescape", codecs.surrogateescape_errors)
        codecs.register_error("surrogatepass", codecs.surrogatepass_errors)

        # Test the 'ignore' error handler
