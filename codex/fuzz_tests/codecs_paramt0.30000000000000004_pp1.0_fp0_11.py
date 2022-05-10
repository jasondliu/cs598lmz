import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.longMessage = True

    def test_01(self):
        """
        Test that the basic functionality works.
        """

        # Create a new instance of the plugin class to test.
        x = csv_to_json.csv_to_json()

        # Give the plugin some data.
        x.set_input_string('a,b,c\n1,2,3\n4,5,6')

        # Run the plugin.
        x.run()

        # Verify that the expected output was created.
        self.assertEqual(x.get_output(), '[{"a": "1", "b": "2", "c": "3"}, {"a": "4", "b": "5", "c": "6"}]')

    def test_02(self):
        """
        Test that the basic functionality works.
        """

        # Create a new instance of the plugin class to test.
