import bz2
bz2.decompress(bz2_data)

# Use bz2.decompress() to decompress the compressed data and store the result in uncompressed_data.
# Make sure when you call bz2.decompress() you use the keyword argument compressionlevel=9.
# The argument compressionlevel=9 is an advanced usage that will provide the best compression.
# It may take a bit longer to run but should finalize with a much smaller file.
# Store the result in uncompressed_data.

# Decompress the data and store the result in uncompressed_data.
uncompressed_data = bz2.decompress(bz2_data, compressionlevel=9)

# Print the length of the uncompressed data to the shell.
print("The uncompressed data is {} bytes long.".format(len(uncompressed_data)))

# Write the uncompressed data to the file uncompressed_data.txt.
# Make sure to use the argument mode='wb' when you call open().
# This will ensure that the file is opened in binary mode.

# Open a new file in write binary
