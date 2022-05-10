import codecs
# Test codecs.register_error('myerror', MyError)
# EncodeError: 'myerror' codec can't encode characters in position 0-1:
# custom error message
#
# Test codecs.register_error('myerror', MyError1)
# EncodeError: 'myerror' codec can't encode character u'\u20ac' in position
# 0: custom error message
#
# Test codecs.register_error('myerror', MyError2)
# EncodeError: 'myerror' codec can't encode character u'\u20ac' in position
# 0: strict error handler


def test_encode_decode_error_handler():

    def encode_error(exc):
        if isinstance(exc, UnicodeEncodeError):
            str = ''.join(map(unichr, exc.object[exc.start:exc.end]))
            return str, exc.end
        else:
            return codecs.charmap_encode(exc.object, exc.encoding, exc.
                errors)


    def decode_error(exc):
        if isinstance(exc,
