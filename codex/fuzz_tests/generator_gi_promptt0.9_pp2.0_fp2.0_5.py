gi = (i for i in ())
# Test gi.gi_code

next(gi)

# Test gi.__qualname__

str(gi)
import datetime

datetime.date.today().weekday()
class TestAttributes:

    def test_attributes(self):
        self.assertTrue(hasattr(self.something, 'time'))

    def test_fake(self):
        self.assertTrue(False)
    def func1(self):
        print(123)
    def func2(self, object_argument):
        """
        Args:
            object_argument: this is argument
        """
        print(123)
    def test_func1(self):
        """Test func1.
        A multiline description
        """
        self.func1()
    def test_func2(self):
        """Test func2.
        Another multiline description
        """
        self.func2(object())
test = TestAttributes()
test.test_func1()
test.test_func2()
test.test_fake()
test.test_attributes()
try:
    import
