import bz2
bz2.compress('hello, this string will be compressed')

# The smallest value in the string is a space, so it is the least frequently occuring 
# character. Therefore, the space gets encoded in 1 bit and the other characters get 
# encoded in more bits. The result is a compressed string of 65 bytes (in Python 2.5)
import zipfile
zipfile.ZipFile('smaller_file.zip', 'w', zipfile.ZIP_DEFLATED).write('original_file')

# The zip module has a few settings, letting us choose between speed and better 
# compression levels. The default is zipfile.ZIP_DEFLATED, which combines the LZMA 
# and Huffman encoding techniques. ZIP_STORED only applies the DEFLATE algorithm 
# (described in RFC1951), which is fast but offers relatively poor compression ratios.

# Bibliographic info
# Kevin C. O'Kane (2012), Data Compression: the complete reference - 4th edition. 
# Springer. ISBN 978-0-387-09670-7

# Ian H. Witten, Alistair
