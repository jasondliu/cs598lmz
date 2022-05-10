import bz2
bz2_compressor = bz2.BZ2Compressor()
data1 = input_file.read(50)
while data1:
    data2 = bz2_compressor.compress(data1)
    if data2:
        output_file.write(data2)
    data1 = input_file.read(50)
output_file.close()
data3 = bz2_compressor.flush()
print(f'Last compress data:{data3}')

with bz2.BZ2File('example.bz2', 'wt') as output_file:
    output_file.write('Contents go here')
    output_file.close()

with bz2.BZ2File('example.bz2') as compressed:
    original = compressed.read()

print(f'Original: {original}')
