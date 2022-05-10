import lzma
# Test LZMADecompressor.

# Create a decompressor object.
decompressor = lzma.LZMADecompressor()

# Feed one byte at a time to the decompressor.
# This will raise an EOFError when the end of the compressed data
# has been reached.
with open('lzma_compressed', 'rb') as input:
    with open('lzma_uncompressed', 'wb') as output:
        while True:
            try:
                data = input.read(1024)
            except EOFError:
                break
            if not data:
                break
            output.write(decompressor.decompress(data))

# Flush the decompressor to get any remaining data.
output.write(decompressor.flush())
</code>

