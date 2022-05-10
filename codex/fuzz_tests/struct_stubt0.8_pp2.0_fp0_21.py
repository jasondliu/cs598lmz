from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4

# Disable buffering to get a traceback on these objs
if sys.version_info[0] >= 3:
    sys.stdout = sys.stderr = Unbuffered(sys.stdout)

class TestPickleUnpickle(unittest.TestCase):
    def test_pickle_unpickle(self):
        headers = (
            (
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36'
            ),
            (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0'
            ),
            (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:48.0) Gecko/20100101 Firefox/48.0'
            ),
           
