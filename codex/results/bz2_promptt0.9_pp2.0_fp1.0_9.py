import bz2
# Test BZ2Decompressor if you want to use the BZ2 output format
if hasattr(bz2, "BZ2Decompressor"):
    class TestBZ2Decompressor(unittest.TestCase):
        def test_from_source(self):
            source = BytesIO(b"foo bar")
            compress = bz2.BZ2Decompressor()
            self.assertEqual(compress.decompress(b"BZh91AY&SY"), b"foo bar")
            self.assertEqual(compress.decompress(b"BZhamo-"), b"")

        @unittest.skipUnless(threading, 'Threading required for this test.')
        def test_lock_init(self):
            compress = bz2.BZ2Decompressor()
            self.assertIsInstance(compress.decompress, collections.Callable)
            self.assertIsInstance(compress._lock, threading.LockType);
            self.assertTrue(compress._lock.acquire(False))
            compress._lock.release()

       
