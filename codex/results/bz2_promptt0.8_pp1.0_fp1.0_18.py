import bz2
# Test BZ2Decompressor and BZ2Compressor classes
import io
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
empty = b''

# use utility functions to test out BZ2Compressor and BZ2Decompressor
bz2.decompress(bz2.compress(data)) == data

# Test .bz2 and .tbz2 files

f = bz2.open(TESTFN, 'wt')
try:
    f.write(TEXT_LINES[0])
    f.write(TEXT_LINES[1])
finally:
    f.close()

f = bz2.open(TESTFN, 'rt')
try:
    assert f.readline() == TEXT_LINES[0]
    assert f.readline() ==
