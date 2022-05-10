import _struct
# Test _struct.Struct objects
import test.string_tests

class StrTest(unittest.TestCase):
    def test_lower(self):
        self.assertEqual('hello'.lower(), 'hello')
        self.assertEqual('Hello'.lower(), 'hello')
        self.assertEqual('HellO'.lower(), 'hello')
        self.assertEqual('hello'.lower(), 'hello')
        self.assertEqual('hellO'.lower(), 'hello')
        self.assertEqual('HeLlO'.lower(), 'hello')
        self.assertEqual(''.lower(), '')

    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')
        self.assertEqual('Hello'.upper(), 'HELLO')
        self.assertEqual('HellO'.upper(), 'HELLO')
        self.assertEqual('hellO'.upper(), 'HELLO')
        self.assertEqual('HeLlO'.upper(), 'HELLO')
        self.assertEqual(''.upper(), '')

