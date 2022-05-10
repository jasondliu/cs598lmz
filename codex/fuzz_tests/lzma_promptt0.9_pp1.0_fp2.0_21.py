import lzma
# Test LZMADecompressor
sample_input = io.BytesIO(mcf_raw_data)
with lzma.LZMADecompressor() as decompressor:
    with closing(decompressor.decompress(sample_input)) as sample_output:
        print(sample_output)
sample_input = io.BytesIO(mcf_raw_data)
with lzma.LZMADecompressor() as decompressor:
    with closing(decompressor.decompress(sample_input, limit=2 ** 32)) as sample_output:
        print(sample_output)
# Compression
sample_input = io.BytesIO(b"Hello world!")
with closing(lzma.LZMACompressor(format=lzma.FORMAT_XZ, check=lzma.CHECK_CRC64, preset=6)) as compressor:
    with closing(compressor.compress(sample_input)) as sample_output:
        print(sample_output)
print(lzma.LZMAError.MEMLIMIT_ERROR)
print(lzma.
