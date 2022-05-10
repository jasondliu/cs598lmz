import lzma
# Test LZMADecompressor.__init__
#
# Make sure that LZMADecompressor.__init__() accepts the same arguments
# as lzma.LZMACompressor.__init__() and that the arguments are passed
# to the underlying LZMADecompressor object.
LZMA_OPTIONS = {'preset': 9, 'format': lzma.FORMAT_RAW, 'check': lzma.CHECK_CRC64}
LZMA_FILTERS = [{'id': lzma.FILTER_LZMA1, 'dict_size': 2 ** 20, 'lc': 3, 'lp': 0, 'pb': 2, 'mode': lzma.MODE_NORMAL}]
