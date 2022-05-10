import bz2
bz2.decompress(data)

# Do BZ2 decompression.
#
# Convert the results to a bytes object (not str!) by adding a b to the front of the string literal.
#
# >>> data = bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
# >>> print(data)

# uncompress.py

import bz2
uncompressed_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(bz2.
