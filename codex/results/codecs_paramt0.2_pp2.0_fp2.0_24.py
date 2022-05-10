import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test_Csv_Writer(unittest.TestCase):

    def test_write_csv(self):
        """
        Test that the csv writer writes the correct data
        """
        # Create a temporary file to write to
        with tempfile.NamedTemporaryFile(delete=False) as f:
            # Write the data to the file
            write_csv(f.name, ['a', 'b', 'c'], [[1, 2, 3], [4, 5, 6]])

        # Read the data back in
        with open(f.name, 'r') as f:
            # Read the data back in
            reader = csv.reader(f)
            # Convert the data to a list
            data = list(reader)

        # Check that the data is correct
        self.assertEqual(data, [['a', 'b', 'c'], ['1', '2', '3'], ['4', '5', '6']])

        # Delete the temporary file
        os.remove(f.name
