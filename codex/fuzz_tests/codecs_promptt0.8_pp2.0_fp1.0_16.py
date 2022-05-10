import codecs
# Test codecs.register_error()
class Test_register_error:
    def test_register_error(self):
        def newignore(exception):
            return (u'', exception.end)

        codecs.register_error('test.ignore', newignore)
        result = codecs.decode('\x80some text', 'ascii', 'test.ignore')
        assert result == u'some text', result

        def newreplace(exception):
            return (u'\uDC80', exception.end)

        codecs.register_error('test.replace', newreplace)
        result = codecs.decode('\x80some text', 'ascii', 'test.replace')
        assert result == u'\uDC80some text', result

        def newbackslashreplace(exception):
            return (u'\\\\', exception.end)

        codecs.register_error('test.backslashreplace', newbackslashreplace)
        result = codecs.decode('\x80some text', 'ascii', 'test.backslashreplace')
        assert result == u
