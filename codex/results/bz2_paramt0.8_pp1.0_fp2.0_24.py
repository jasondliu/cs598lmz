from bz2 import BZ2Decompressor
BZ2Decompressor()
#from bz2 import decompress
#decompress
#bz2.BZ2File
from bz2 import BZ2File
f = open("file.dat", "rb")
bzf = BZ2File('file.dat.bz2', 'w')
bzf.write(f.read())
bzf.close()
f.close()
from bz2 import BZ2File
f = open("file.dat", "rb")
bzf = BZ2File('file.dat.bz2', 'w')
bzf.write(open("file.dat", "rb").read())
bzf.close()
f.close()
from bz2 import BZ2File
f = BZ2File('file.dat.bz2', 'w')
f.write(open("file.dat", "rb").read())
f.close()
import bz2
bz2.compress("Hello World!")
bz2.compress("HelloWorld!")
bz2.compress("Hello"}
bz
