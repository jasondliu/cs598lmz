import lzma
# Test LZMADecompressor and LZMACompressor

import unittest, os, time, sys
import lzma

verbose = 0

def hextext(text):
    return ':'.join(x.encode('hex') for x in text)

# Return the file size and a file object
def getsize(filename):
    st = os.stat(filename)
    size = st.st_size
    f = open(filename, 'rb')
    return size, f

class TestLZMA(unittest.TestCase):

    def setUp(self):
        self.chunksize = 1024*256
        # self.chunksize = 1024*256
        self.data = self.source = None
        self.decomp_data = self.decomp_source = None

    def tearDown(self):
        if self.source:
            self.source.close()
        if self.data:
            self.data.close()
        if self.decomp_source:
            self.decomp_source.close()
