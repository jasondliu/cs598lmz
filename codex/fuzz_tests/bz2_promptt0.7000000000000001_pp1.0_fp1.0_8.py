import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with open('data/sample_bz2', 'rb') as compressed_input:
    sample_data = compressed_input.read()
    sample_data_decompressed = decompressor.decompress(sample_data)
print(sample_data_decompressed)

with open('data/sample_bz2', 'rb') as compressed_input:
    with open('data/sample_bz2_decompressed', 'wb') as decompressed_output:
        decompressor = bz2.BZ2Decompressor()
        for chunk in iter(lambda: compressed_input.read(100), b''):
            decompressed_output.write(decompressor.decompress(chunk))

import bz2
with open('data/sample_bz2', 'rb') as compressed_input:
    with open('data/sample_bz2_decompressed', 'wb') as decompressed_output:
        decompressor = bz2.BZ2Decompressor()
        while True:
