import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)

import json
import sys

def __get_data():
    raise ImportError('Failed to import module')

data = dict()
try:
    data = __get_data()
except ImportError:
    pass

class TestString(unittest.TestCase):
    """Tests for the the 'string' keyword"""

    def test_keyword_exists(self):
        self.assertIn('string', data["keywords"])

    def test_keyword_type(self):
        string = data["keywords"]["string"]
        self.assertIn('type', string)
        self.assertIn('items', string['type'])
        self.assertEqual('string', string['type']['items'])

    def test_keyword_minLength(self):
        string = data["keywords"]["string"]
        self.assertIn('minLength', string)
        self.assertIn('type', string['minLength'])
        self.assertEqual('integer', string['minLength'
