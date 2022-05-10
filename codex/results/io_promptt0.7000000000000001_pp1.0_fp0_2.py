import io
# Test io.RawIOBase class

class RawIOTest(unittest.TestCase):

    def test_rawiobase(self):
        # This is a mixin class which has no tests of its own
        pass

def test_main():
    test.support.run_unittest(RawIOTest)

if __name__ == '__main__':
    test_main()
