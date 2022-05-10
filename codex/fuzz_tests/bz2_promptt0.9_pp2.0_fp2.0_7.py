import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
d.decompress(open(path, 'rb').read()) == open(path + '.bz2', 'rb').read()

# Test bz2.decompress
bz2.decompress(open(path + '.bz2', 'rb').read()) == open(path + '.bz2', 'rb').read()

# Test bz2.BZ2File
bz2.BZ2File(path + '.bz2').read() == open(path,'rb').read()

# Test bz2.open with rb
bz2.open(path + '.bz2', 'rb').read() == open(path,'rb').read()

# Test bz2.open with rt
bz2.open(path + '.bz2', 'rt').read()

# Test bz2.open with r
bz2.open(path + '.bz2', 'r').read()

# Test bz2.open without mode
bz2.open(path + '.
