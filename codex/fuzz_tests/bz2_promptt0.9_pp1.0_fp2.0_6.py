import bz2
# Test BZ2Decompressor object API
decomp = bz2.BZ2Decompressor()

# Show what methods the decompressor object has
#print([method for method in dir(decomp) if callable(getattr(decomp, method))])

# Create a BZ2File object with mode='r'
# This will return a decompression stream
# bz2file is an iterable that produces bytes
bz2file = bz2.BZ2File(input_file, 'r')

# Initialize an empty byte string to hold our decompressed data
data = b''

# Decompress and append each 1024 byte chunk into data
# When the decompression stream reaches the end of the file,
# it produces empty bytes b''
# Iterate until you reach the end
for chunk in iter(lambda: bz2file.read(1024), b''):
    data += decomp.decompress(chunk)
data

# Print out the first 5000 bytes of data
# The Wikipedia document starts with this tag
#print(data[:5000])

# Close the BZ2File object
bz2
