import codecs
# Test codecs.register_error

from test import support
from test.support import import_fresh_module

from test.test_support import TESTFN, check_warnings, run_with_locale
from test.test_support import verbose

# We need to use a non-ascii filename
testfilename = TESTFN + '\u00e4'
testfilename_other_encoding = TESTFN + '\xe4'

class CodecRegistrator:
    def __init__(self):
        self.codecs = [
            'test.test_codecs.testcodec',
            'test.test_codecs.testutf8',
            'test.test_codecs.testcodec_streamreader',
            'test.test_codecs.testcodec_streamwriter',
        ]

    def __enter__(self):
        for modname in self.codecs:
            mod = import_fresh_module(modname)
            mod.register()
        return self

    def __exit__(self, *args):
        for modname in self.cod
