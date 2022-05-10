import bz2
# Test BZ2Decompressor class
dec = bz2.BZ2Decompressor()
print(dec.decompress(b'BZh91AY&SY\xc4\x0f\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))
 
# Test BZ2Compressor class
comp = bz2.BZ2Compressor();
print(comp.compress(b"hello world!"))
