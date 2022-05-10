import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('data/text/enwik8.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content[:10])
    print(bz2_decompressor.decompress(file_content)[:10])

print('\n')

with open('data/text/enwik8.bz2', 'rb') as f:
    for chunk in iter(lambda: f.read(100), b''):
        print(chunk[:10])
        print(bz2_decompressor.decompress(chunk)[:10])
        print('\n')

print('\n')

with open('data/text/enwik8.bz2', 'rb') as f:
    decompressed_data = b''
    for chunk in iter(lambda: f.read(100), b''):
        decompressed_data += bz2_decompressor.decompress(chunk)
   
