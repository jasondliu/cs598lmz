import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time
with open('lorem.xz', 'rb') as input:
    with open('lorem.txt', 'wb') as output:
        while True:
            # Read a block of data
            block = input.read(1024)
            if not block:
                break

            # Decompress the block of data
            uncompressed = decompressor.decompress(block)

            # If the uncompressed data is larger than
            # the block of data, append the uncompressed
            # data to the output file
            if uncompressed:
                output.write(uncompressed)

            # If the end of the compressed data has
            # been reached, stop looping
            if decompressor.eof:
                break

# Close the files
input.close()
output.close()
 
# Print the contents of the decompressed file
with open('lorem.txt', 'r') as f:
    print(f.read())

# Delete
