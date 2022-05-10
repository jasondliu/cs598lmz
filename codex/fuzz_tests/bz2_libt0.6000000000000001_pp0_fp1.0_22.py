import bz2
bz2.decompress(bz2_data)

# You can compress data in one shot too, or just one line at a time.
uncompressed_data = b"Lots of content here"
compressed = bz2.compress(uncompressed_data)
compressed

# bz2.decompress(compressed)

# You can also use a text mode with bz2.

# bz2_data = bz2.compress(text_data)
# bz2.decompress(bz2_data).decode('utf-8')

# Compressing data with bz2 can be 20-100x as slow as with zlib, but the
# resulting data is much smaller.

# ## Python 3.4+ includes the zlib.compress() and zlib.decompress() functions
# that have a simpler interface compared with the clunky zlib module. You’ll
# still need to import zlib, but you can use the functions as follows:

import zlib
s = b'witch which has which witches wrist watch'
len(
