from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")

# in bz2.py, BZ2Decompressor.decompress
self._buffer = self._buffer + self._decompressor.decompress(data, size)

# in bz2.py, BZDecompressor.decompress
result = self._decompress(data)

# in bz2.py, BZ2Decompressor._decompress
if len(self._buffer) > 0:
    # start by using any data left over from the previous call
    data = self._buffer + data
    self._buffer = b''
if len(data) == 0:
    return b''
else:
    # make sure that the compressed data buffer is large enough to
    # hold
