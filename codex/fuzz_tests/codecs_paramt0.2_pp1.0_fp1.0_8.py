import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class TestCase(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.longMessage = True

    def test_00(self):
        """
        Test the basic functionality of the module.
        """
        #
        # Create a test file.
        #
        with open('test.txt', 'w') as f:
            f.write('This is a test.\n')
            f.write('This is a test.\n')
            f.write('This is a test.\n')
            f.write('This is a test.\n')
            f.write('This is a test.\n')
            f.write('This is a test.\n')
            f.write('This is a test.\n')
            f.write('This is a test.\n')
            f.write('This is a test.\n')
            f.write('This is a test.\n')
            f.write('This is a
