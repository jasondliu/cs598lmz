import mmap
# Test mmap.mmap(-1, size)

# Test mmap.mmap(-1, size)

class MmapTests(unittest.TestCase):

    def test_constructor(self):
        size = 1024
        m = mmap.mmap(-1, size)
        self.assertEqual(len(m), size)
        m.close()

    def test_size(self):
        size = 1024
        m = mmap.mmap(-1, size)
        self.assertEqual(m.size(), size)
        m.close()

    def test_find(self):
        m = mmap.mmap(-1, 0)
        m.write(b"foo")
        self.assertEqual(m.find(b"foo"), 0)
        self.assertEqual(m.find(b"bar"), -1)
        m.close()

    def test_move(self):
        m = mmap.mmap(-1, 0)
        m.write(b"foo")
        m.seek(0)
        self.assertEqual
