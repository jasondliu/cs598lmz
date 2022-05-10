import codecs
codecs.register_error('strict', codecs.ignore_errors)

###############################################################################

class Test_Base(unittest.TestCase):
    '''
    Base class for tests.
    '''

    def setUp(self):
        '''
        Initialize.
        '''
        self.maxDiff = None
        self.longMessage = True

    def check_output(self, expected, actual):
        '''
        Check expected against actual, with optional line-by-line comparison.
        '''
        if isinstance(expected, list):
            self.assertEqual(expected, actual)
        else:
            self.assertEqual(expected.splitlines(), actual.splitlines())

###############################################################################

class Test_00(Test_Base):
    '''
    Test case for the 00_start.py file.
    '''

    def test_00(self):
        '''
        Test the 00_start.py file.
        '''
        import 00_start
        self.check_output(EXPECTED_00, 00_start.
