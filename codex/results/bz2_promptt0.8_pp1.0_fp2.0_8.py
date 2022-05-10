import bz2
# Test BZ2Decompressor() object.
# No need to include in final program.
bz = bz2.BZ2Decompressor()
bz.decompress(compressedString)

# Compare to compressed file.
# No need to include in final program.
fo = open(fileName + '.bz2', 'wb')
fo.write(compressedString)
fo.close
