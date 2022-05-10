import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SY.\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xff\xff\xff\x01\x00?'
bzd = bz2.BZ2Decompressor()
bzd.decompress(data)
