import codecs
# Test codecs.register_error()


class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error()
        def strict_errorhandler(exception):
            raise exception

        def ignore_errorhandler(exception):
            return u'', exception.end

        def replace_errorhandler(exception):
            return u'?', exception.end + 1

        def xmlcharrefreplace_errorhandler(exception):
            if not isinstance(exception, UnicodeEncodeError):
                raise TypeError(
                    "don't know how to handle %r" % exception)
            return (u'&#%d;' % exception.object[exception.start],
                    exception.end)

        def bad_errorhandler1(exception):
            return u'?'

        def bad_errorhandler2(exception):
            return u'', exception.end, exception.end + 1

        def bad_errorhandler3(exception):
            return u'', exception.end, u'extra'

        # Test the default behavior
        for encoding in
