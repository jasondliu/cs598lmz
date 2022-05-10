import codecs
# Test codecs.register_error()

import codecs
import unittest

class CodecsModuleTest(unittest.TestCase):
    def test_register_error(self):
        # Testing the various forms of codecs.register_error()
        def errhandler_1(exception):
            return (u"", exception.end)
        def errhandler_2(exception):
            return (u"", exception.end+1)
        def errhandler_3(exception):
            return (u"\ufffd", exception.end)
        def errhandler_4(exception):
            return (u"\ufffd", exception.end+1)

        for err in [u"strict", u"ignore", u"replace", u"xmlcharrefreplace",
                    u"backslashreplace", errhandler_1, errhandler_2,
                    errhandler_3, errhandler_4]:
            codecs.register_error(u"test_register_error", err)
