import lzma
# Test LZMADecompressor.

from lzip import LZMAFile

from test_lzma import FILES, open_files

def _test_decompressor(decompressor, lzma_mode, input_size=None,
                       memlimit=None):
    for name, filename, data in open_files(FILES, mode=lzma_mode):
        if input_size is not None:
            data = data[:input_size]
        x = decompressor.decompress(data, memlimit=memlimit)
        y = uncomp_data(filename)
        assert x == y

def test_simple_decompressor():
    for lzma_mode in '-el', '--format=xz':
        for input_size in 1, 100, 1000, 10000, 100000, 1000000, 10000000:
            _test_decompressor(lzma.LZMADecompressor(), lzma_mode, input_size)

def _test_lzma_file():
    for name, filename, data in open_files(FILES, mode='-
