fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

#
# Test string formatting
#

class TestStringFormatting:

    def test_format_string(self):
        self.assertEqual(
            '{0} {1}'.format('one', 'two'),
            'one two'
        )

    def test_format_string_empty(self):
        self.assertEqual(
            '{0} {1}'.format('one'),
            'one '
        )
