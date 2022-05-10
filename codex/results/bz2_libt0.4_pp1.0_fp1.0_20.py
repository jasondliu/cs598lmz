import bz2
bz2.decompress(bz2_compressed).decode('utf-8')

# Exercise: Decompress the bz2 file and extract the wiki markup text
#
# The bz2 file is compressed using the bz2 algorithm.  Decompress the
# file using the bz2.decompress() function and decode the result using
# the utf-8 encoding.
#
# The bz2.decompress() function takes a single parameter, which is the
# compressed data, and returns the decompressed data.
#
# The result of bz2.decompress() is binary data, which must be
# decoded using the utf-8 encoding to get a string.
#
# Your function should return a single string containing the markup
# of the Wikipedia article.
#
# Hint: Don't forget to close the file!
#
# Hint: The Wikipedia article is in the file BZh91AY&SY.txt,
#       which is already open for you.
#
# Hint: You can read the whole file into a single byte string
#       using f.
