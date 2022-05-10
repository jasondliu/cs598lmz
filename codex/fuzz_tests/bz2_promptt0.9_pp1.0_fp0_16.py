import bz2
# Test BZ2Decompressor:


class TestBZ2Decompressor(unittest.TestCase):

    def bz2check(self, testdata, blocksize=None, output=None):
        with bz2.BZ2File(testdata, 'rb') as f:
            data = f.read()
        d = bz2.BZ2Decompressor()
        f = BytesIO(data)
        x = []
        if blocksize is None:
            for block in iter(lambda : f.read(100), b''):
                x.append(d.decompress(block))
            x.append(d.decompress())
        else:
            while True:
                block = f.read(blocksize)
                if block == b'':
                    break
                x.append(d.decompress(block))
        if output is None:
            return b''.join(x)
        else:
            return x[output]
        return

    def test_decompress(self):
        for testdata in 'cheeseshop.bz2', 'j
