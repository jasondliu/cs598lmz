import bz2
bz2.BZ2File('compressed.bz2', 'w')

#compress_opts is a tuple with compress level (0-9) as first option and the 
#second option is 0 for ZLIB and 1 for BZIP2 compression
bz2_compressor = bz2.BZ2Compressor(compresslevel = 9)
compressed_data = bz2_compressor.compress(string_to_compress)
more_compressed_data = bz2_compressor.compress(some_other_string)
bz2_compressor.flush()

#extracting tar archives using tarfile library
import tarfile
tar = tarfile.open('sample.tar')
tar.extractall()
tar.close()

#for creating tar archive
import tarfile
tar = tarfile.open('sample.tar')
for name in ['file1.txt', 'file2.txt', 'file3.txt']:
    tar.add(name)
tar.close()

#specify compression mode
tar = tarfile.open('sample.
