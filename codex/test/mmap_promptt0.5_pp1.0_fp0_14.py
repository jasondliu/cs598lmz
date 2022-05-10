import mmap
# Test mmap.mmap(0, 1, "", mmap.ACCESS_READ)

class TestMMap(unittest.TestCase):
    def setUp(self):
        self.filename = tempfile.mktemp()
        f = open(self.filename, 'w+b')
        try:
            f.write(bytes(bytearray(range(256))))
        finally:
            f.close()
