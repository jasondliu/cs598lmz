from bz2 import BZ2Decompressor
BZ2Decompressor()
#print(BZ2Decompressor())

# bytes
s= 'hello'
s[0]
#s.decode('utf') error
#s.encode('utf') error
#str.encode(s,'utf')

# iterable
l=[1,2,3]
i=iter(l)
next(i)
next(i)
next(i)
