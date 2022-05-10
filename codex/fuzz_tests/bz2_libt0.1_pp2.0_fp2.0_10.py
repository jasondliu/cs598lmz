import bz2
bz2.decompress(bz2.compress(b'hello world'))

# bz2.compress() returns bytes, and bz2.decompress() requires bytes.

# The compress() and decompress() functions both accept an optional parameter, compresslevel, which can be an integer between 1 and 9 specifying the level of compression: 1 produces the least compression, and 9 (default) produces the most compression.

# A higher compresslevel means more compression, but also means that compression will take more time.

# The bz2 module also includes a convenience function, open(), that works like the open() function in the built-in open() function, but opens bzipped files.

# The open() function accepts an optional parameter, compresslevel, that works just like the compresslevel parameter to the compress() function.

# The open() function returns a file object, and the usual methods are available for reading or writing compressed data.

# The following example shows how to read a bzipped file one line at a time without decompressing the entire file into memory:

import bz2
un = b'BZh91AY&SY
