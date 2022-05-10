import _struct
# Test _struct.Struct.format_size()

class S(object):
    def __init__(self, format):
        self.format = format

def format_size(obj):
    return _struct.Struct(obj.format).format_size()

class TestStruct(unittest.TestCase):
    def test_format_size(self):
        self.assertEqual(format_size(S("")), 0)
        self.assertEqual(format_size(S("i")), _struct.calcsize("i"))
        self.assertEqual(format_size(S("ii")), _struct.calcsize("ii"))
        self.assertEqual(format_size(S("iii")), _struct.calcsize("iii"))

def test_main():
    support.run_unittest(__name__)

if __name__ == "__main__":
    test_main()
