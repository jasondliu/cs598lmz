import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # This test is not exhaustive, but it should catch most of the
        # problems.
        def bad_handler(exception):
            raise RuntimeError
        def good_handler(exception):
            return (u'', 0)
        def bad_handler2(exception):
            return (u'', 0, 1)
        def bad_handler3(exception):
            return (u'', 0, None)
        def bad_handler4(exception):
            return (u'', 0, u'')
        def bad_handler5(exception):
            return (u'', 0, u'', 1)
        def bad_handler6(exception):
            return (u'', 0, u'', None)
        def bad_handler7(exception):
            return (u'', 0, u'', u'')
