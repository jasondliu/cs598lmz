import bz2
# Test BZ2Decompressor.inflate()
compressed = bz2.compress(b'Hello there')
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SY.\x00\x00\x008\x00\x00\x00!\x00\x00\x00P\x80\x00\x00\x00\x00\x00\x00\x00d\x80\x00\x00\x00')
'Hello there'
decompressor.decompress(b'BZh91AY&SY.\x00\x00\x00\x01\x00\x00\x00%\x80\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x04')
'Hello there'
decompressor.decompress(b'BZh91AY&SY.\x00\x00\x00\x01\x00\x
