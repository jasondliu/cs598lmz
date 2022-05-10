import lzma
# Test LZMADecompressor class (based on test_lzma module)
import zlib

from unittest import TestCase, skipUnless

from distork import _lzma as lzma

SAMPLES = [
    [ 0x777a170b1a, 0x26730d914e, 0x40b46bb97f, 0x7cc2f44673 ],
    [ 0xfb1a50d9ed, 0x6c4cf4e4f4, 0x0d15afc5e5, 0x5f5a95971d, 0x764291eecb ],
    [ 0x750b1a777a, 0x30d914e267, 0xb46bb97f40, 0xc2f446737c ],
    [ 0x1a50d9edfb, 0x4cf4e4f4e4, 0x15afc5e5e5, 0x5a95971d7f, 0x4291eecb76 ],
    [ 0x0b1a777a17, 0xd914e267
