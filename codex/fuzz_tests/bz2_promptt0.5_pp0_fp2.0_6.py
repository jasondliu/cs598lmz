import bz2
# Test BZ2Decompressor class
decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f_input:
    with open('data/enwik8_decompressed.txt', 'wb') as f_output:
        while True:
            block = f_input.read(1024)
            if not block:
                break
            uncompressed = decompressor.decompress(block)
            if uncompressed:
                f_output.write(uncompressed)
            else:
                break
        # Check if any data left in the buffer
        remaining = decompressor.unconsumed_tail
        if remaining:
            f_output.write(remaining)

# Test BZ2File class
with bz2.BZ2File('data/enwik8.bz2', 'rb') as f_input:
    with open('data/enwik8_decompressed.txt', 'wb') as f_output:
        for data in iter(lambda: f_input.read(100 * 1024), b''):
           
