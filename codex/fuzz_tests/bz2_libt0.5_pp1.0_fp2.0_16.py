import bz2
bz2_file = bz2.BZ2File('test.bz2', 'rb')
bz2_file.read(100)

bz2_file_uncompressed = bz2.BZ2File('test.bz2', 'rb')
bz2_file_uncompressed.read(100)

bz2_file_uncompressed.seek(0)
bz2_file_uncompressed.read(100)

bz2_file_uncompressed.seek(0)
bz2_file_uncompressed.read(100)

bz2_file.seek(0)
bz2_file.read(100)

bz2_file.seek(0)
bz2_file.read(100)

bz2_file.seek(0)
bz2_file.read(100)

bz2_file.seek(0)
bz2_file.read(100)

bz2_file.seek(0)
bz2_file.read(100)

