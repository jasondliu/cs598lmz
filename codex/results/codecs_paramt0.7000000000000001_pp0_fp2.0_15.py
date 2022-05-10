import codecs
codecs.register_error('surrogate_or_unsafe', codecs.replace_errors)

class Test_Convert_Date(unittest.TestCase):
    """
    Test the Convert_Date function
    """
    def test_Convert_Date(self):
        """
        Test the Convert_Date function
        """
        # Test with the string format
        result = Convert_Date(datetime.datetime(2015, 1, 1, 0, 0))
        # We don't care about fractions of seconds
        self.assertEqual(result[:19], "2015-01-01T00:00:00")

        # Test with the string format
        result = Convert_Date(datetime.date(2015, 1, 1))
        # We don't care about fractions of seconds
        self.assertEqual(result[:19], "2015-01-01T00:00:00")

        # Test with the time format
        result = Convert_Date(datetime.time(0, 0))
        # We don't care about fractions of seconds
        self.assertEqual(result[:19],
