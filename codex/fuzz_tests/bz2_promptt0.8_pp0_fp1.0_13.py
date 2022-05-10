import bz2
# Test BZ2Decompressor with a stream containing only the bzip2 end-of-stream (EOS) marker.
# This previously generated an error similar to "Unable to decompress data; code -1 = \
# BZ_UNEXPECTED_EOS".
t = bz2.BZ2Decompressor()
t.decompress(b'BZh91AY&SY\x0b\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x0b\x00')
# Test BZ2Decompressor.decompress() with some valid bzip2 data followed by an EOS
t = bz2.BZ2Decompressor()
input_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9
