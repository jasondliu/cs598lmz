import bz2
bz2.compress(b"This is a test")

# Decompress
bz2.decompress(
    b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
)

# Compress a file
with open('lorem.txt', 'rb') as input:
    with bz2.BZ2File('lorem.txt.bz2', 'wb', compresslevel=9) as output:
        output.writelines(input)

# Decompress a file
with bz2.BZ2File('lorem.txt.bz2', 'rb') as input:
    with open('lorem2.txt', 'wb') as output:
        for line in input:
            output.write(line)

# Compress a file using a context manager
with bz2.BZ2File('lorem.txt
