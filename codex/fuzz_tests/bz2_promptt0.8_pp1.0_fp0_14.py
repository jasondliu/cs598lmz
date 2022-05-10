import bz2
# Test BZ2Decompressor
uncompressed_data = b'Hello World\n'
compressed = bz2.compress(uncompressed_data)
decompressor = bz2.BZ2Decompressor()
s = decompressor.decompress(compressed)
print(s)

decompressor.unused_data

data = b'Some uncompressed data'
try:
    decompressor.decompress(data)
except EOFError as err:
    print('Not enough data to decompress')
    
print('Unused data:', decompressor.unused_data)
# Test BZ2File

with open('lorem.txt', 'rb') as input:
    with bz2.open('lorem.txt.bz2', 'wb') as output:
        output.write(input.read())
    
with bz2.open('lorem.txt.bz2', 'rt') as compressed:
    for line in compressed:
        print(line, end='')
        
with bz2.open('lorem.txt.bz2', '
