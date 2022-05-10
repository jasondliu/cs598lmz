import bz2
# Test BZ2Decompressor as source
with open('uncompressed.dat', 'wb') as result:
    with bz2.BZ2File('compressed.dat', 'rb') as uncompress:
        d = bz2.BZ2Decompressor()
        for chunk in iter(lambda : uncompress.read(1000), b''):
            result.write(d.decompress(chunk))
# Test bz2.open as context manager
with bz2.open('compressed.dat', 'rb') as infile,\
     open('uncompressed.dat', 'wb') as outfile:
    for chunk in iter(lambda : infile.read(1000), b''):
        outfile.write(d.decompress(chunk))
import bz2
import sys
opener = bz2.open
bz2.open = bz2.BZ2File
sys.modules['_bz2'].open = bz2.BZ2File
open('uncompressed.dat', 'wb').write(d.decompress(open('compressed.dat', '
