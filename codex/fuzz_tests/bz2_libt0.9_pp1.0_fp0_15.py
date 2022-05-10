import bz2
bz2ob = bz2.BZ2File('./data/file/comp.bz2', 'wb')
bz2ob.write('compress me')

bz2ob.close()

bz2ob = bz2.BZ2File('./data/file/comp.bz2', 'rb')
print(bz2ob.read(2))
print(bz2ob.read())
bz2ob.close()
try:  
    bz2ob = bz2.BZ2File('./data/file/comp.bz2', 'r')
    print(bz2ob.read())
finally:  
    bz2ob.close()
#compress using bz2.compress
import bz2
s = '''i am a very big and long string that i expect bz2 can compress it, the question is how much it will be compressed?
by the way'''

c = bz2.compress(s)
print(c)
print(bz2.decompress(c))


