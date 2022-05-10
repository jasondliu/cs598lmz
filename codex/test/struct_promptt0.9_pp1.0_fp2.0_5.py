import _struct
# Test _struct.Struct("My", mysize, "= 3s2pc")

class readlineTestCase(unittest.TestCase):
    def test_basic(self):
        buffer = self.f.readline()
        self.failUnlessEqual(buffer, "abc\n")
        buffer = self.f.readline(10)
        self.failUnlessEqual(buffer, "12345,67890\n")
        buffer = self.f.readline(5)
        self.failUnlessEqual(buffer, "abcde")
        buffer = self.f.readline()
        self.failUnlessEqual(buffer, "fghijk\n")
        buffer = self.f.readline(4)
        self.failUnlessEqual(buffer, "lmno")
        buffer = self.f.readline()
        self.failUnlessEqual(buffer, "pqrstuvwxyz\n")
        buffer = self.f.readline(1000)
        self.failUnlessEqual(buffer, "")

