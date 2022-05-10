import codecs
# Test codecs.register_error functions and codecs.lookup_error function.
import codecs

class CodecRegressionTest(unittest.TestCase):

    def test_codecs_error_registry(self):

        # We test CodecInfo.errors functionalities by using the "replace"
        # error handler.
        def my_decode(msg):
            return (u"*", msg.count("x"))
        codecs.register_error("test.replace", my_decode)
        self.assertEqual(b'abxcdx'.decode("ascii", "test.replace"), u'*2')

        # Test the case where you register an error handler with a different
        # casing to an already existing one.
        def my_decode2(msg):
            return (u"!", msg.count("x"))
        codecs.register_error("test.Replace", my_decode2)
        # The behavior which one should expect here is probably not defined in
        # the codecs module.
        # If one uses the codec lookup function with a different casing, the
        # codec
