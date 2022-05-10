import bz2
# Test BZ2Decompressor.

# Decompress a file.
cmode = bz2.COMPRESSION_STANDARD

# Decode with the same mode used to create the source file.
with bz2.open('sample.bz2', mode='rt',
              encoding='utf-8', compresslevel=cmode) as fin:
    with open('sample.txt', mode='w') as fout:
        fout.writelines(fin)

# Decode with the any contemporary decompression mode.
with bz2.open('sample.bz2', mode='rt',
              encoding='utf-8') as fin, open('sample.txt', mode='w') as fout:
    fout.writelines(fin)

# Create a BZ2Decompressor object.
decompressor = bz2.BZ2Decompressor()
with open('sample.bz2', 'rb') as fin, open('sample.txt', 'wb') as fout:
    while True:
        block = fin.read(1024)
        if not block:
            break
        fout.
