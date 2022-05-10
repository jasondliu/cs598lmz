import codecs
# Test codecs.register_error

import sys

class CodecTest(unittest.TestCase):
    # The UnicodeEncodeError and UnicodeDecodeError are raised with
    # the following constructor call:
    # Unicode(En|De)codeError(encoding, object, startindex, endindex, reason)
    # 'reason' is optional.

    # Tests for UnicodeEncodeError

    def test_UnicodeEncodeError(self):
        # EncodeError constructor
        err = UnicodeEncodeError('ascii', u'hello', 0, 2, 'ouch')
        self.assertEqual(err.encoding, 'ascii')
        self.assertEqual(err.object, u'hello')
        self.assertEqual(err.start, 0)
        self.assertEqual(err.end, 2)
        self.assertEqual(err.reason, 'ouch')
        # XXX Should we test the traceback argument as well?

        # Error message
        self.assertRaisesMessage(UnicodeEncodeError,
            "'ascii' codec can't encode characters in position
