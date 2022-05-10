import codecs
# Test codecs.register_error
# XXX Can this be extended to support writing to a file via a StringIO object
# XXX instead of the real thing?

class Test_codecs:
    
    def test_bad_register_error(self):
        """Check a few bad arguments to register_error"""
        assertRaises(TypeError, codecs.register_error, None)
        assertRaises(TypeError, codecs.register_error, "g")
        assertRaises(TypeError, codecs.register_error, "g", None)

