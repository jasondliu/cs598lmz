import lzma
# Test LZMADecompressor with various filters.

def test_simple():
    data = b'\x00' * 10
    for filters in [
            [{'id': lzma.FILTER_LZMA1,
              'dict_size': 2**16,
              'lc': 0,
              'lp': 0,
              'pb': 0,
              'mode': 0,
              'nice_len': 128,
              'mf': lzma.MF_HC4,
              'depth': 0}],
            [{'id': lzma.FILTER_LZMA1,
              'dict_size': 2**16,
              'lc': 0,
              'lp': 0,
              'pb': 0,
              'mode': 0,
              'nice_len': 128,
              'mf': lzma.MF_HC3,
              'depth': 0}],
            [{'id': lzma.FILTER_LZMA1,
              'dict_size': 2**16,
              'lc': 0,
              'lp': 0,
              '
