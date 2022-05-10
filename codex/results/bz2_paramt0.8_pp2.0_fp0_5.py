from bz2 import BZ2Decompressor
BZ2Decompressor(s)

s = "Hello world"
import zlib
zlib.decompress(s)
zlib.decompressobj(s)

s = "Hello world"
import zlib
print zlib.crc32(s)
print zlib.adler32(s)

s = "Hello world"
import zlib
zlib.compress(s)
zlib.compressobj(s)

s = raw_input()
print s

s = raw_input("Type something: ")
print "I read this from the user: ", s

s = input()
print s

s = input("Type something: "
