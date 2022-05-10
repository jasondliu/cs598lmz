import codecs
# Test codecs.register_error
class Test_register_error(unittest.TestCase):
    encoding = 'xyzzy'
    def test_register_error(self):


        # register an error handling function

        def g(exception):
            return (u'', exception.end)
        codecs.register_error(Test_register_error.encoding, g)
        # test the function
        s = u'\udcaa\udc02'
        self.assertRaises(UnicodeDecodeError, s.encode, Test_register_error.encoding)
        r = '\\udcaa\\udc02'.encode(Test_register_error.encoding)
        self.assertEqual(r, '\\udcaa')

        # register again
        def h(exception):
            return (u'*', exception.end)
        codecs.register_error(Test_register_error.encoding, h)
        # test the new function
        s = u'\udcaa\udc02'
        r = '\\udcaa\\udc02'.
