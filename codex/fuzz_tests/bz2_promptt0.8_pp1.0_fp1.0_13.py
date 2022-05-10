import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('../../data/pi_million_digits.bz2', 'rb') as input_file:
    # Read file in 4k chunks
    for data in iter(lambda: input_file.read(4096), b''):
        print(decompressor.decompress(data), end='')

print()


# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('../../data/sample_text.txt', 'rb') as input_file:
    # Read file in 4k chunks
    for data in iter(lambda: input_file.read(4096), b''):
        output_data = compressor.compress(data)
        if output_data:
            print(output_data, end='')

print()
