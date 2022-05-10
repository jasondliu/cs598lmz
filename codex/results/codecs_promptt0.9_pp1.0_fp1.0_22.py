import codecs
# Test codecs.register_error
import unicodedata
from test import support


class CodecTestMixin(object):
    create_decoder = None
    create_encoder = None

    class MyDecodingError(UnicodeError):
        pass
    test_error = MyDecodingError

    def test_decode_with_errors(self):
        # Test the handling of error parameter
        my_errors = 'strict'
        # ascii codec handles spanish
        s = 'a\xe1\xd1b'
        iso8859_1_expected = u"a\xe1\xd1b"
        utf8_expected = u"a\xc3\xa1\xc3\x91b"
        for encoding in ('ascii', 'iso8859-1', 'utf-8'):
            for errors in ('strict', 'ignore', 'replace'):
                try:
                    decoded = self.decode(s, encoding, errors)
                except UnicodeError as exc:
                    decoded = str(exc)
                expected = eval('%s_expected' % encoding.
