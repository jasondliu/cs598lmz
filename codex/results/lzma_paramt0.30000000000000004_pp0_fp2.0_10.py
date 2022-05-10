from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# b'The quick brown fox jumps over the lazy dog.'
</code>

<code>import lzma

with open('file.xz', 'rb') as f:
    file_content = lzma.decompress(f.read())
</code>

