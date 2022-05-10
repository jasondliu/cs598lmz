import bz2
# Test BZ2Decompressor on a file

# Open the file
with bz2.open('example.bz2', 'rb') as input:
    print('File opened')

    try:
        # Wrap the decompressor with an BufferedReader for efficient reading
        decompressor = bz2.BZ2Decompressor()
        with io.BufferedReader(input) as buffered_input:

            while True:
                # Decompress one block
                block = buffered_input.read(1024 * 1024)
                if not block:
                    print('End of compressed data')
                    break
                data = decompressor.decompress(block)
                if data:
                    # Process the data
                    ...
                    print('Processed %d bytes of decompressed data' % len(data))
                else:
                    # End of stream
                    print('No more decompressed data')
                    break
    finally:
        print('Closing')

# Close the file

# Output:
# File opened
# Processed 1048576 bytes of decompressed data
# Processed 1048576 bytes of decompressed data
# Process
