import codecs
# Test codecs.register_error() with the 'surrogateescape' error handler.
# Copied from Lib/test/test_codecs.py

import unittest

class RegisterReadTest(unittest.TestCase):
    # Do exactly what codecs.py does for surrogateescape

    def setUp(self):
        self.oldcode = sys.getfilesystemencoding()
        sys.setfilesystemencoding('ascii')
        try:
            import encodings
        except ImportError:
            try:
                import codecs
            except ImportError:
                # Python 2.2, 2.3 and 2.4 don't have encodings
                if sys.platform == 'win32' or sys.platform.startswith('os2'):
                    self.encoding = 'mbcs'
                else:
                    self.encoding = 'ascii'
            else:
                self.encoding = codecs.lookup(sys.getfilesystemencoding()).name
