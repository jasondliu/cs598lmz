import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time
with open('lorem.xz', 'rb') as input:
    while True:
        # Read a block of data
        block = input.read(1024)
        if not block:
            break
        # Decompress the block
        text = decompressor.decompress(block)
        # If the decompressor needs more input, it will raise an exception
        # (LZMAError)
        # If the decompressor has finished, it will return an empty byte string
        if text:
            print(text)

# The decompressor object can be used again after it has finished
# decompressing the stream
# This is useful if you want to decompress multiple streams with the same
# decompressor object

# Read one byte at a time
with open('lorem.xz', 'rb') as input:
    while True:
        # Read a block of data
        block = input.read(1024)
        if not block:
            break

