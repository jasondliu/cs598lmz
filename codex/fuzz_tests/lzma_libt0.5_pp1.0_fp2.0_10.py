import lzma
lzma.LZMADecompressor().decompress(e)

## 'X'

## We can see that the compression algorithm is LZMA, and the compression level is 9.

## We can use the `lzma` module to decompress the data.

## We can also use the `lzma` module to compress data.

lzma.LZMACompressor(format=lzma.FORMAT_ALONE, check=lzma.CHECK_CRC64, preset=9).compress(b"X")

## b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x00\x04\x00\x00\x00'

## You can see that the output is different, because the `lzma` module uses a different
## format (the `lzma` module supports the legacy `.lz
