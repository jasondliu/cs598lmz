from lzma import LZMADecompressor
LZMADecompressor().decompress(b'x\x9c\x8cW\xcf,\xcdM\xce\xcf\xccK\x04\x82\r\x00\x8f')

# Use the new in-file API
with open(filename, 'rb') as f:
    decompressor = LZMADecompressor()
    with decompressor.read_from(f) as decompressed:
        pass

# Compress data using the default compression level
LZMACompressor().compress(data)

# Compress data using the highest compression level
LZMACompressor(preset=9).compress(data)
