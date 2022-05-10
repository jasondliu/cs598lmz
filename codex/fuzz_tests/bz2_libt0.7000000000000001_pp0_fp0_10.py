import bz2
bz2_file = bz2.BZ2File('data/python.bz2')
print 'read 5 bytes from BZ2 file:', bz2_file.read(5)
bz2_file.close()

# write to BZ2 file
bz2_file = bz2.BZ2File('data/write_bz2.bz2', 'w')
bz2_file.write('this is a BZ2 file')
bz2_file.close()

# check if a file is BZ2 compressed
import bz2
file_name = 'data/python.bz2'
is_compressed = bz2.BZ2File.is_bz2file(file_name)
print 'is ' + file_name + ' compressed?', is_compressed

# compress/decompress BZ2 file with context manager
import bz2
uncompressed_data = 'this is some uncompressed data'
with bz2.BZ2File('data/python.bz2', 'w') as fout:

