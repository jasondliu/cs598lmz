import lzma
lzma.LZMAFile

# We don't have the python-lzma package on the buildbots, so we can't actually
# test this.
#
# from lzma import LZMAFile
#
# class TestLZMAFile(TestCase):
#     def test_read(self):
#         with open(TESTFN, 'wb') as f:
#             f.write(b'a' * 10000)
#             f.write(b'b' * 10000)
#         with open(TESTFN, 'rb') as f:
#             with LZMAFile(f) as x:
#                 # This should be the same as reading a file
#                 data = x.read()
#                 self.assertEqual(data, b'a' * 10000 + b'b' * 10000)
#                 # This should be the same as reading a file in chunks
#                 x.seek(0)
#                 data = b''
#                 for i in range(100):
#                     data += x.read(100)
#                 self.assertEqual(data
