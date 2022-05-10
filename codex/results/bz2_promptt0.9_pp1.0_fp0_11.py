import bz2
# Test BZ2Decompressor -->
fd = open('files/example2.bz2', 'rb')
decompressor = bz2.BZ2Decompressor()

while True:
    compressed = fd.read(10)
    if not compressed:
        break
    uncompressed = decompressor.decompress(compressed)
    print(uncompressed)

uncompressed = decompressor.flush()
print(uncompressed)
fd.close()

# BZ2File --->

print()
print()
print('---------------------')
print('      BZ2File       ')
print('---------------------')

print('ou abro com BZ2File')
fd = bz2.BZ2File('files/example2.bz2')
fp = decompressor.decompress(fd)
print(fp)


# TextIOWrapper -->


print()
print()
print('---------------------')
print('  TextIOWrapper     ')
print('---------------------')


print('ou posso até os 2 de uma vez')
fd = open
