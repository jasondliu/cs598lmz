import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()
print(bz2_decompressor.decompress(bz2_data))

# Test BZ2File
bz2_file = bz2.BZ2File('bz2_file.bz2', 'wb')
try:
    bz2_file.write(b'This is the data to be compressed. ' * 100)
finally:
    bz2_file.close()

bz2_file = bz2.BZ2File('bz2_file.bz2', 'rb')
try:
    print(bz2_file.read())
finally:
    bz2_file.close()

# Test open()
with bz2.open('bz2_file.bz2', 'rb') as bz2_file:
    for line in bz2_file:
        print(line)
