import lzma
# Test LZMADecompressor class

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time
with open('test.xz', 'rb') as input:
    with open('test.out', 'wb') as output:
        while True:
            compressed = input.read(1)
            if not compressed:
                break
            data = decompressor.decompress(compressed)
            if data:
                output.write(data)
            else:
                break

# Verify that the output file is identical to the input file
with open('test.out', 'rb') as f:
    print(f.read() == b'This is the input data.\n')
