import bz2
# Test BZ2Decompressor
# https://stackoverflow.com/questions/3288595/multiprocessing-using-pool-map-on-a-function-defined-in-a-class
# https://stackoverflow.com/questions/17158492/python-multiprocessing-pool-with-instance-method

class BZ2Decompressor(object):
    def __init__(self):
        self.decompressor = bz2.BZ2Decompressor()

    def decompress(self, data):
        return self.decompressor.decompress(data)

    def flush(self):
        return self.decompressor.flush()

def test_bz2_decompressor():
    # Test BZ2Decompressor
    bz2_decompressor = BZ2Decompressor()
