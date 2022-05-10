import mmap
# Test mmap.mmap.resize and mmap.mmap.move
class TestResizeAndMove(unittest.TestCase):
    def test_resize(self):
        for size in range(0, 1024, 1):
            with open(TESTFN, 'wb') as f:
                f.write(b'\0' * size)
            with open(TESTFN, 'rb') as f:
                m = mmap.mmap(f.fileno(), 0)
                self.assertEqual(len(m), size)
                self.assertEqual(m.size(), size)
                m.resize(0)
                self.assertEqual(len(m), 0)
                self.assertEqual(m.size(), 0)
                m.resize(size)
                self.assertEqual(len(m), size)
                self.assertEqual(m.size(), size)
            with open(TESTFN, 'rb') as f:
                m = mmap.mmap(f.fileno(), 0)
                self.assertEqual(len(m
