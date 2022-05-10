import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

decompressor.decompress(compressed_data)

# Decompress the data in 'compressed_file' and store the results in 'uncompressed_file'.
# Make sure to close the files at the end.
with bz2.open('compressed_file', 'rb') as input, open('uncompressed_file', 'wb') as output:
    for data in iter(lambda: input.read(100 * 1024), b''):
        output.write(decompressor.decompress(data))
    output.write(decompressor.flush())
 
import operator
# for unique values
d={1:2,2:4,3:6}; operator.itemgetter(0)(d)

# for sorting 
sorted(d.items(), key=operator.itemgetter(0))
sorted(d.items(), key=operator.itemgetter(1))

# for sorting on multiple attributes
student_tuples  = [('john', 'A', 5),
                   ('j
