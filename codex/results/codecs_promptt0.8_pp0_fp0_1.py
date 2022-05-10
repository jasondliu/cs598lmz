import codecs
# Test codecs.register_error()
import encodings
from encodings import iso8859_3, iso8859_15, mbcs, utf_16_be, utf_16_le
import string, sys

verbose = 0

class CodecRegistryError(Exception):
    pass

def search_function(encoding):
    # force all errors to raise LookupError
    codecs.register_error("strict", lambda x: x)
    try:
        return codecs.lookup(encoding)
    except LookupError:
        return None

class CodecsModuleTest(unittest.TestCase):

    def test_aliases_cache(self):
        # This test should not raise a SystemError due to aliasing the
        # sys.modules dictionary.
        encodings.aliases.aliases

    def test_register_error(self):
        if verbose: print 'test register_error'
        #
        # test exception callbacks
        #
        # start off with a known lookup table
        codecs.register_error("test", codecs.lookup
