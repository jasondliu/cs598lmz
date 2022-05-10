import lzma
lzma.LZMAFile

class LZMAFile(lzma.LZMAFile):
    def __init__(self, filename, mode="r", format=None, check=-1, preset=None, filters=None):
        if format is None:
            format = lzma.FORMAT_AUTO
        if format == lzma.FORMAT_AUTO:
            format = lzma.FORMAT_XZ
        super(LZMAFile, self).__init__(filename, mode, format, check, preset, filters)

def main():
    import sys
    import os
    import time
    import numpy as np
    import bcolz
    import lzma
    import bcolz_lzma

    N = int(1e7)
    cparams = bcolz.cparams(cname='blosclz', clevel=5, shuffle=bcolz.SHUFFLE, cbytes=1e6)
    a = np.arange(N, dtype='i4')

    t0 = time.time()
   
