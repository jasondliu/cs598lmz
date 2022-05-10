import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
decomp.decompress(data)

import lzma
# Test LZMADecompressor with multiple decompress() calls
decomp = lzma.LZMADecompressor()
decomp.decompress(data[:100])
decomp.decompress(data[100:])

import lzma
# Test LZMADecompressor with multiple decompress() calls
decomp = lzma.LZMADecompressor()
decomp.decompress(data[:100])
decomp.decompress(data[100:])

import lzma
# Test LZMADecompressor with multiple decompress() calls
decomp = lzma.LZMADecompressor()
decomp.decompress(data[:100])
decomp.decompress(data[100:])

import lzma
# Test LZMADecompressor with multiple decompress() calls
decomp = lzma.LZMADecompressor()
