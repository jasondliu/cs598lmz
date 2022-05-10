import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
# Constants
#

#
# Functions
#

#
# Classes
#

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass


if __name__ == '__main__':
    unittest.main()
