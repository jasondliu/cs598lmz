import io
# Test io.RawIOBase.readinto()
from array import array
from io import BytesIO, BufferedReader
import _io

class MyBytesIO(BytesIO):
    def __len__(self):
        return self.getbuffer().nbytes

class TestRawIOBase:
    data = b"hello world\nhow are you?\n"

    def test_readinto(self):
        b = MyBytesIO(self.data)
        a = array("b", b" " * len(self.data))
        n = b.readinto(a)
        self.assertEqual(a.tobytes(), self.data)
        self.assertEqual(n, len(self.data))

        # Read byte at a time
        b = MyBytesIO(self.data)
        a = array("b", b" " * len(self.data))
        for i in range(len(a)):
            a[i:i+1] = b.readinto(a[i:i+1])[0]
