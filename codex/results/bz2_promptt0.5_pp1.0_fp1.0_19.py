import bz2
# Test BZ2Decompressor

#
# Create a decompressor object
#
d = bz2.BZ2Decompressor()

#
# Decompress one line at a time and print
#
for line in bz2_file:
    print(d.decompress(line))

#
# Close the file
#
bz2_file.close()

#
# Create a decompressor object
#
d = bz2.BZ2Decompressor()

#
# Decompress the entire file
#
uncompressed_data = d.decompress(bz2_data)

#
# Close the file
#
bz2_file.close()

#
# Print the result
#
print(uncompressed_data)
 
#
# Create a decompressor object
#
d = bz2.BZ2Decompressor()

#
# Decompress the entire file
#
uncompressed_data = d.decompress(bz2_data)

#
# Close the file
#
bz2_file.
