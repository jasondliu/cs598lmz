import codecs
# Test codecs.register_error
import _codecs

class codecs_test:
    def test_register_error_normal(self):
        def replacement_error(exc):
            if isinstance(exc, UnicodeDecodeError):
                return (u'\ufffd', exc.end)
            elif isinstance(exc, UnicodeEncodeError):
                return (u'\ufffd'.encode('utf-8'), exc.end)
            else:
                raise TypeError("don't know how to handle %r" % exc)

        self.assertEqual(sys.stdout.encoding, "utf-8")
        old_handler = codecs.lookup_error('strict')
        codecs.register_error('test.strict', replacement_error)
        new_handler = codecs.lookup_error('test.strict')
        self.assertIsNot(new_handler, old_handler)
        self.assertEqual(new_handler(UnicodeEncodeError('ascii', u'\xe9', 0, 1, 'ouch')),
                         ('\xc3\
