import codecs
# Test codecs.register_error() with a bogus error handler


def codec_error_registration_encode(input, errors):
    raise UnicodeDecodeError(errors, input, 0, len(input), 'message')


def codec_error_registration_decode(input, errors):
    raise UnicodeEncodeError(errors, input, 0, len(input), 'message')


class CodecsRegisterErrorTest(unittest.TestCase):

    def test_bogus(self):
        '''
        # make sure we can register bogus error handlers
        '''
        self.assertRaises(LookupError, codecs.register_error,
            'bogus', lambda arg: arg)
        self.assertRaises(LookupError, codecs.register_error,
            'bogus', lambda arg: arg)

    def test_encode(self):
        '''
        # make sure we can register encoder error handlers
        '''
        codecs.register_error('test.encode', codec_error_registration_encode)
        self.assertRaises(Unicode
