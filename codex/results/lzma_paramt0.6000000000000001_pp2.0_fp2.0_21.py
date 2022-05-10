from lzma import LZMADecompressor
LZMADecompressor().decompress(data)  # b'This is the text.'
#lzma.decompress(data)

#------------------------------------------------------------------------------
#                               Compress
#------------------------------------------------------------------------------

from lzma import LZMACompressor
compressor = LZMACompressor(format=lzma.FORMAT_ALONE,
                            check=lzma.CHECK_CRC64,
                            preset=9 | lzma.PRESET_EXTREME)
chunk = compressor.compress(b'This is the text.')
chunk += compressor.flush()

#------------------------------------------------------------------------------
#                               Compress and Decompress
#------------------------------------------------------------------------------

from lzma import LZMACompressor
compressor = LZMACompressor(format=lzma.FORMAT_ALONE,
                            check=lzma.CHECK_CRC64,
                            preset=9 | lzma.PRESET_EXTREME)
chunk = compressor.compress(b'This is the text.')
chunk += compressor.flush()

print(chunk)

from
