import lzma
# Test LZMADecompressor will decompress data
class TestLZMADecompressor(unittest.TestCase):
    def test_decompress(self):
        
        def read_bytes(io_obj):
            return bytearray(io_obj.read())

        with open('lzma_sample_files/lzma2.txt', 'rb') as f:
            print(len(f.read()))
        
        with open('lzma_sample_files/lzma2.txt', 'rb') as f:
            x = lzma.LZMADecompressor()
            a = read_bytes(x.decompress(f.read()))

        with open('lzma_sample_files/lzma2.txt.udata', 'rb') as f:
            b = read_bytes(f)
        
        print(len(a))
        print(len(b))
        self.assertEqual(a,b)
    
    def test_decompress_from_file(self):
        
        def read_bytes(io
