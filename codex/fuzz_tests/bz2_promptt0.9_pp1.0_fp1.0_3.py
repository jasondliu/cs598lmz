import bz2
# Test BZ2Decompressor.peek()
decompressor = BZ2Decompressor()
self.assertEqual(decompressor.peek(1), decompressor.unconsumed_tail[0:1])
self.assertEqual(decompressor.peek(1), b'')
decompressor.decompress(self.dummydata)
self.assertEqual(decompressor.peek(1), self.text[0:1])
self.assertEqual(decompressor.peek(), self.text)
decompressor.decompress(b'\wrongstuff')
self.assertRaises(BZ2Decompressor.EOF_MARKER, decompressor.peek, 1)
# Test BZ2Decompressor.unconsumed_tail
decompressor = BZ2Decompressor()
decompressor.decompress(self.dummydata)
self.assertEqual(decompressor.unconsumed_tail, self.text)
decompressor.decompress(b'X' * 100)
self.assertEqual(decompressor.un
