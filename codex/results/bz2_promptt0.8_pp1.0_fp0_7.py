import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

compressed_file = open(path_to_bz2_file, "rb")
compressed_file.read(5) # skip the first 5 bytes

# decompress the rest
data = decompressor.decompress(compressed_file.read())

# if the file is not corrupted, the decompressed data will end in "</mediawiki>"
assert data.endswith("</mediawiki>")

# close the file and release resources held
compressed_file.close()
 
# Test BZ2File

compressed_bz2_file = bz2.BZ2File(path_to_bz2_file)

# read 5 bytes, the same as before
data = compressed_bz2_file.read(5)

# read the rest of the compressed file
data = compressed_bz2_file.read()

# close the file and release resources held
compressed_bz2_file.close()
 
# Test to doublecheck

uncompressed_
