import bz2
# Test BZ2Decompressor
# http://stackoverflow.com/questions/27981545/suppress-warning-unclosed-file-<_io-bufferedreader-name-rb-at-0x7f25d0c5b438
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    decompressor = bz2.BZ2Decompressor()
