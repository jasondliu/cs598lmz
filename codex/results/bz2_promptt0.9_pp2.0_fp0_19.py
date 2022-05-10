import bz2
# Test BZ2Decompressor class
# Reads compressed file as input, and outputs decompressed file
compressedFile = bz2.BZ2File('exampleFile.bz2', 'rb')
decompressor = bz2.BZ2Decompressor()

output = decompressor.decompress(compressedFile.read())
output = output.decode('utf-8')
print(output)

compressedFile.close()

newFile = open('decompressedFile.txt', 'w')
newFile.write(output)
newFile.close()

# File is successfully decompressed and the output is written to a new file.

# As an iterable, BZ2File class may be used to read data one line at a time instead of loading
# entire file in memory all at once.
# There is a common use of iterating over lines in a file.
# A similar method can be used to work with a compressed file.
compressedFile = bz2.BZ2File('exampleFile.bz2', 'rb')

for line in compressedFile:
    print(line)

compressed
