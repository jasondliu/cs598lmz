import bz2
# Test BZ2Decompressor class:
d = bz2.BZ2Decompressor()
d.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\xac\x10'
            b'\x00\x00\x003\x00 \x003\x00  \x00\x04\x00 \x00'
            b'\x00\x04\x80 \x00\x00\x01\x00 \x00\x00$\x00 \x00'
            b'\x00\x00\x00 \x00\x00\x00\x00 \x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

