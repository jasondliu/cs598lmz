import select
# Test select.select functionality
# Check it works on multiple fd's
# Check timeout is adhered to

# Test a stanadlone select version against python implentation to check accuracy

#  Running test cases:
#  Searching for tests:
#    1.    > python select_tests.py
#    2.    > python -c "import select_tests; select_tests.main()"
#  Running tests:
#    1.    > python -m unittest select_tests
#    2.    > python -c "import select_tests; unittest.main(module=select_tests)"

TIMEOUT_TIME = 1.0

class TestSelect(unittest.TestCase):
    def setUp(self):
        pass

    def test_read_write(self):
        """Test that read and write lists return nonempty after reading and writing
        """
        r,w,x = select.select([self.sock], [self.sock], [], TIMEOUT_TIME)
        self.assert_(self.sock in r)
        self.assert_(self
