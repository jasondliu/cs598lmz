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

        # If the decompressor needs more input,
        # raise an exception
        if decompressor.unused_data:
            raise Exception('Need more data')

        # Do something with the text
        print(text)

# Flush the decompressor
text = decompressor.flush()
print(text)

# Check that the decompressor has finished
if decompressor.unused_data:
    raise Exception('Unexpected extra data')
 
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time
with open('l
