import bz2
# Test BZ2Decompressor.inflate()
c = bz2.BZ2Decompressor()
c.inflate(b"BZ")
c.inflate(b"h")
c.inflate(b"1AY&SY")
c.inflate(b"\x04\x00h\x99\x0bh\x0c\x001\x14\x84\x84\x001\x14\x88\x84\x001\x14\x8c\x80\x00")
c.inflate(b"")
c.inflate(b"BZh9")
c.inflate(b"\x02\x00h\x99\x0bh\x0c\x001\x14\x84\x84\x001\x14\x88\x84\x001\x14\x8c\x80\x00")
c.inflate(b"")

# Test BZ2Decompressor.decompress()
c = bz2.BZ2Decompressor()

