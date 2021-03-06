from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
# b'The quick brown fox jumps over the lazy dog.'

# Compress with a preset
import lzma
compressor = lzma.LZMACompressor(preset=9 | lzma.PRESET_EXTREME)
compressor.compress(b'The quick brown fox jumps over the lazy dog.')
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
