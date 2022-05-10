import bz2
bz2_comp = bz2.BZ2Compressor()

# compressed_data = bz2_comp.compress(plain_text)
# compressed_data += bz2_comp.flush()

compressed_data = bz2.compress(plain_text)
with open('compressed_text.bz2', 'wb') as f:
    f.write(compressed_data)

print(f'Compressed from {len(plain_text)} to {len(compressed_data)}, {(1 - len(compressed_data) / len(plain_text))*100 :.2f}%')

# decompressor =bz2.BZ2Decompressor()
# try:
#     original_text = decompressor.decompress(compressed_data).decode()
# except EOFError:
#     decompressor.decompress(compressed_data)

with open('compressed_text.bz2', 'rb') as fp:
    bz_data = fp.read()
    print(bz2.dec
