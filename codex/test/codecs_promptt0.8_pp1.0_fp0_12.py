import codecs
# Test codecs.register_error
def codec_error_encode_callback(exc):
    if isinstance(exc, UnicodeEncodeError):
        target_charset = exc.encoding
        text = exc.object
        start = exc.start
        end = exc.end
        return u"", start+1

