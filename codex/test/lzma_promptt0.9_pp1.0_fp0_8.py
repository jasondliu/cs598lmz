import lzma
# Test LZMADecompressor

#        lzdecomp = lzma.LZMADecompressor()
#        data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'
#
#        hdr = lzdecomp._read_zlib_header(data[12:])
#        start = hdr["len"] + 6 + 12
#        block = data[start:]
#
#        pos = 0
#        print( hex(lzdecomp._read_compressed_size(block, pos, 64)) )

        #decomp.decompress(block)


import lzma

from itertools import product
