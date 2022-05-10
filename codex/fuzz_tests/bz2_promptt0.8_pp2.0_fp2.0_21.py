import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()
next_line = bz2_decompressor.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14
\xe1BA\x06\xbe\x084')
next_line += bz2_decompressor.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\
\xe1BBP\x91\xf08')
print(next_line)

# Read files in BZ2 Compression format

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image:
