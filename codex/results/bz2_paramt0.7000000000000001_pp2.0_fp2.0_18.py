from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.decompress(open("data.bz2","r").read()))

#import bz2
#t = bz2.compress(data)
#print t
#data = bz2.decompress(t)
#print data
#bz2.decompress(t)
#print data

#import gzip
#data = gzip.compress(data)
#print data
#data = gzip.decompress(data)
#print data
