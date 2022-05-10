import codecs
# Test codecs.register_error('testIgnore', TestIgnoreHandler)


class TestIgnoreHandler(codecs.StreamReader):
    def __init__(self, stream, errors='strict'):
        super(TestIgnoreHandler, self).__init__(stream, errors)

    def decode(self, input, errors="strict"):
        return (
            Codecs__decoder_encode_to_utf8__128n(input, errors),
            len(input)
        )

    def reset(self):
        Codecs__streamreader_reset(self)
