import codecs
# Test codecs.register_error() with a custom error handling class that
# inserts forbidden characters in encodings that encode that character to
# a forbidden byte.

# Uncomment the next line to see the exception that triggers.
#codecs.register_error('strict', codecs.ignore_errors)

class ForbidUmlauts(object):
    codec_forbid_codes = b'\xae'

    def __init__(self):
        self.codec_forbidden = {
            'utf-7': (b'+', b'-', b'&'),
            'utf-8': (b'\xef\xbf\xae'),
            # This test doesn't test UTF-16 much, because the error
            # handler doesn't get called for error characters in the
            # surrogate range.
            #'utf-16': (b'\xff\xfe', b'\xff\xff'),
        }

    def encode(self, exc):
        exc.object[exc.end] = self.codec_forbidden[exc.encoding][0]
        return (exc.object[exc.
