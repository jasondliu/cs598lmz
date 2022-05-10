import bz2
# Test BZ2Decompressor

# Create a BZ2Decompressor object
decompressor = bz2.BZ2Decompressor()

# Read one byte, decompress it, and write the output
with open('sample.bz2', 'rb') as input, open('uncompressed.txt', 'wb') as output:
    while True:
        # Read a byte
        byte = input.read(1)
        if not byte:
            break
        # Decompress the byte
        char = decompressor.decompress(byte)
        # Write the output
        output.write(char)

# Flush the decompressor
unused_data = decompressor.flush()
 
# Print the number of bytes of unused data
print('Unused data:', len(unused_data))

# Print the contents of the unused data
print(unused_data)

# Print the contents of the original file
with open('sample.bz2', 'rb') as input:
    print(input.read())

# Print the contents of the decompressed file
with open('uncompressed.txt
