import codecs
# Test codecs.register_error to replace default error handling
# of codecs.encode and codecs.decode.

import codecs
import types

# A test error class
class CodecTestError(Exception):
    pass

# Error handling callback
def codec_test_err(error):
    if isinstance(error, UnicodeError):
        codec = error.encoding
        obj = error.object
        start = error.start
        end = error.end
        raise CodecTestError("Encoding Error %s %s %s" %
                             (codec,obj,(start,end)))
    elif isinstance(error, UnicodeDecodeError):
        codec = error.encoding
        obj = error.object
        start = error.start
        end = error.end
        raise CodecTestError("Decoding Error %s %s %s" %
                             (codec,obj,(start,end)))
    else:
        raise CodecTestError("Unknown Error %s" % error)

# Test the error handling callback
