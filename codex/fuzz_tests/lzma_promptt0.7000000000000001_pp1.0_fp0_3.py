import lzma
# Test LZMADecompressor
import io
lzma_decomp = lzma.LZMADecompressor()
lzma_decomp.decompress(codecs.encode(data, 'latin-1'))

# You can also do the same thing with io.BytesIO
file = io.BytesIO(codecs.encode(data, 'latin-1'))
lzma_decomp.decompress(file.read())
</code>

