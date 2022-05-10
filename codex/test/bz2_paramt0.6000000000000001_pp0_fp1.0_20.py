from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# Create a file in your current directory called ‘test.txt’ with the compressed data above.
# Write a program that reads the file, decompresses it, and checks that it matches the original uncompressed data.
# Use the bz2.BZ2Decompressor class.

with open('test.txt', 'wb') as f:
    f.write(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

with open('test.txt', 'rb') as f:
    data = f.read()
   
