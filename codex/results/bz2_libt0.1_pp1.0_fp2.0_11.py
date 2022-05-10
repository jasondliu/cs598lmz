import bz2
bz2.decompress(bz2.compress(b'Hello World'))

# bz2.compress() returns a bytes object, and bz2.decompress() requires a bytes-like object.
# So you need to make sure you’re using the right type in each place.

# The compress() and decompress() functions both accept an optional parameter, compresslevel,
# which can be an integer between 1 and 9 specifying the level of compression.
# A value of 1 represents the fastest compression, while a value of 9 represents the best compression.
# The default value is 9.

# The bz2 module also includes a useful utility function for getting the size of the compressed data.
# The bz2.compress() function returns the compressed data, but it also requires extra memory to do so.
# If you want to get the size of the compressed data without using extra memory, use the bz2.compress_size() function instead.

import bz2
original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)
compressed
