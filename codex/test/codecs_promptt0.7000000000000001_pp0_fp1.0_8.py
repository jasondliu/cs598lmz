import codecs
# Test codecs.register_error
# Error handling with unknown codec name
import codecs

def codec_error_handler(exception):
    return ("", exception.end)

codecs.register_error("test.error", codec_error_handler)

