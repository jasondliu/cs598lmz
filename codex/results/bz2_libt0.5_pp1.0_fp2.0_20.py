import bz2
bz2.decompress("BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")

# ord()
# ord(c) is the integer representing the Unicode code point for the character c.
# This is the inverse of chr().
# ord('a')
# 97
# ord('€')
# 8364
# chr(8364)
# '€'

# unichr()
# unichr(i) is the Unicode string representing the character whose encoding is the integer i.
# This is the inverse of ord() for Unicode strings.
# unichr(8364)
# u'\u20ac'
# unichr(128406)
# u'\U0001f34e'

# bz2.decompress("BZh91AY&SYA\xaf\x82
