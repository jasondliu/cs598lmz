import bz2
# Test BZ2Decompressor
'''
from cStringIO import StringIO
dec = bz2.BZ2Decompressor()
decompressed_data = StringIO()

file_name = 'regex_sum_672881.txt.bz2'
file_handle = bz2.BZ2File(file_name)
for line in file_handle:
    result = dec.decompress(line)
    decompressed_data.write(result)
file_handle.close()
print decompressed_data.getvalue()
'''

# Test BZ2Compressor
from cStringIO import StringIO
comp = bz2.BZ2Compressor()
compressed_data = StringIO()

file_name = 'regex_sum_672881.txt'
file_handle = open(file_name)
for line in file_handle:
    result = comp.compress(line)
    compressed_data.write(result)
result = comp.flush()
compressed_data.write(result)

file_handle.close()
print compressed_data.getvalue
