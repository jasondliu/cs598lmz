import codecs
# Test codecs.register_error() with a bogus error handler


def codec_error_registration_encode(input, errors):
    raise UnicodeDecodeError(errors, input, 0, len(input), 'message')


def codec_error_registration_decode(input, errors):
    raise UnicodeEncodeError(errors, input, 0, len(input), 'message')


