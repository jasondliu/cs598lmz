import lzma
# Test LZMADecompressor

with open('lzma_compressed_data.bin', 'rb') as f_in:
    with lzma.open(f_in, 'rb') as f_out:
        while True:
            bytes = f_out.read(4096)
            if not bytes:
                break
            print(bytes)
            # Do something with bytes here

print(str(bytes))

f = open('lzma_decompressed_data.bin', 'wb')
f.write(bytes)
f.close()

print('\nDecompression complete!')

with open('lzma_decompressed_data.bin', 'rb') as f_in:
    with lzma.open(f_in, 'rb') as f_out:
        while True:
            bytes = f_out.read(4096)
            if not bytes:
                break
            print(bytes)
            # Do something with bytes here

print(str(bytes))

f = open('lzma_recompressed_data.bin', 'wb')

