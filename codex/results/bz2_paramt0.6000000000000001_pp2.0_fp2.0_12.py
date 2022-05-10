from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# TODO:
# - parse the data into a datastructure
# - print the data out in a useful way
# - use the datastructure to print out a few more useful things

# The data is in a key-value store format. It's not json, but it's
# similar. It's also compressed, so we'll need to decompress it.

# The key-value store format is as follows:
# - The first byte of the data tells us how many bytes the key is.
# - Then we have the key, followed by the value.
# - The value can be another key-value store, or a list of key-value
#   stores.

# The data is compressed with bzip2, so let's decomp
