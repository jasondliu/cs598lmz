import codecs
# Test codecs.register_error
#
# This test is a bit tricky, because we need to make sure that the
# codecs module is imported before we start registering errors.
#
# The easiest way to do this is to import the codecs module in this
# file, and then import this file from the test_codecs.py file.

class CodecsModuleTest(unittest.TestCase):
    def test_register_error(self):
        # This test is a bit tricky, because we need to make sure that the
        # codecs module is imported before we start registering errors.
        #
        # The easiest way to do this is to import the codecs module in this
        # file, and then import this file from the test_codecs.py file.
        #
        # If this test fails, you probably added a new test case to
        # test_codecs.py that imports the codecs module.  Move the import
        # into this file instead.
        self.assertTrue(codecs.lookup_error('test'))

def test_main():
    test_support.run_unitt
