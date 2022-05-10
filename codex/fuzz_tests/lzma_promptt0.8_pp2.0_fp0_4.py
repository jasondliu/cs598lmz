import lzma
# Test LZMADecompressor's ability to decompress LZMA streams.
import lzmaffi
import _lzma

from tests import test_support
from tests import test_zipimport_support
from test import test_support as support


TESTFN = support.TESTFN
TESTFNDIR = os.path.dirname(TESTFN)

print_max = 512

def print_generated(fromfile, tofile, data):
    print "Input file: %s (%d bytes)" % (fromfile, len(data))
    print "Output file: %s (%d bytes)" % (tofile, len(data))
    if len(data) <= print_max:
        print repr(data)
        print md5.new(data).hexdigest()
    else:
        print md5.new(data[:print_max]).hexdigest()
        print '...'
        print md5.new(data[-print_max:]).hexdigest()


class TestLzma(unittest.TestCase):
    def setUp(self):
        self.smallfile
