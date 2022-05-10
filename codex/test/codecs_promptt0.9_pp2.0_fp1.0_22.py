import codecs
# Test codecs.register_error with bytes-like objects.

register_error = codecs.register_error

class CodecTest:

    def test_register_error_bytes(self):
        # partial substitutes
        REPL = b'X'*8
        self.test = []
        def handle_codec_error(*args):
            self.test.append(args)
            res = REPL[:args[2]]
            if len(args[2]) < len(REPL):
                args[1].write(args[3][len(REPL):])
            return res, args[2]+len(REPL)
        register_error('test', handle_codec_error)
        encoder = codecs.lookup('utf-8')[1]
        self.test = []
        encoder(errors='test')("abc")
        assert self.test == [('utf-8', None, 3, 'abc', 0)], self.test

def test_main():
    import test_support
    test_support.run_unittest(CodecTest)

