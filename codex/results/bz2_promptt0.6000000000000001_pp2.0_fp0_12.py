import bz2
# Test BZ2Decompressor

# Try to decompress a compressed file
with open('lorem.txt.bz2', 'rb') as f_in:
    with bz2.BZ2Decompressor() as decompressor:
        with open('lorem_copy.txt', 'wb') as f_out:
            for block in iter(lambda: f_in.read(100 * 1024), b''):
                f_out.write(decompressor.decompress(block))
# Try to decompress a compressed file
with open('lorem.txt.bz2', 'rb') as f_in:
    with bz2.BZ2Decompressor() as decompressor:
        with open('lorem_copy.txt', 'wb') as f_out:
            while True:
                block = f_in.read(100 * 1024)

                if not block:
                    break

                f_out.write(decompressor.decompress(block))
# Try to decompress a compressed file
with open('lorem.txt.bz2', 'rb') as f_in:
    with
