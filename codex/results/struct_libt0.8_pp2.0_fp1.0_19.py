import _struct

# add the whole directory of sample files
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

# file used for testing
filename_good = os.path.join(os.path.dirname(__file__), "..", "..", "..", 
                             "sample_data", "data", "ua-mac", 'gh0.dat')

class Test_ua_mac(unittest.TestCase):
    """
    Tests the ua-mac data parser.
    """
    def test_parse_success(self):
        """
        Tests parsing a correctly formatted file.
        """
        stream = open(filename_good, 'rb')
        parser = ua_mac.Parser(stream)
        records = [rec for rec in parser]
        
        self.assertEqual(records[0].date, datetime.datetime(2019, 5, 12, 1, 0))
        self.assertEqual(records[0].press, [1008.0, 1008.0
