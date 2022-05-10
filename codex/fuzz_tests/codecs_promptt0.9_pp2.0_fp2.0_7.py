import codecs
# Test codecs.register_error() in the face of missing-newline
# interactions.  Report on SF bug #624775.
from test.test_support import TestFailed, run_unittest
import test.test_support
import unittest


fail_re = re.compile('^(.+: )?Failed to flush')

def output(s):
    sys.stdout.write(s + '\n')
    sys.stdout.flush()

class MissingNewlineTest(unittest.TestCase):

    def test_write_utf8(self):
        encoder = codecs.getincrementalencoder('utf8')()
        output('stdout.encoding: ' + sys.stdout.encoding)
        for s in ['\xc4', 'te\xc4st']:
            try:
                codecs.register_error('test.force_ignore', None)
                res = encoder.encode(s)
            finally:
                codecs.register_error(encoder.errors,
                                      encoder.decode)
            output(u"
