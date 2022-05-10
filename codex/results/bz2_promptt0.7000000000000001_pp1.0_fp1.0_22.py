import bz2
# Test BZ2Decompressor
with bz2.BZ2File('example4.bz2', 'r') as input:
    print(input.read())

# Test BZ2Compressor
data = 'The same line, over and over.\n'
with bz2.BZ2File('example5.bz2', 'w') as output:
    for i in range(100):
        output.write(data)

data = b'Lots of data here.'
with bz2.open('example6.bz2', 'w') as output:
    output.write(data)

with bz2.open('example6.bz2', 'r') as input:
    print(input.read())

with bz2.open('example6.bz2', 'rb') as input:
    print(input.read(500))
# Compressing Data in Memory
import bz2
uncompressed_data = 'The same line, over and over.\n' * 10
uncompressed_data_len = len(uncompressed_data)
print('UNCOMPRESSED
