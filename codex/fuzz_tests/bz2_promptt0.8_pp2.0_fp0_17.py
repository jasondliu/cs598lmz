import bz2
# Test BZ2Decompressor
#

d = bz2.BZ2Decompressor()
d.decompress(open("lzw.py.bz2", "rb").read())

# Test BZ2File
#

print "testing BZ2File"

a = bz2.BZ2File("ash-SunOs5.6-bytecode.py.bz2")

print a.read(100)

print "testing BZ2File(mode='w')"

a = bz2.BZ2File("test5.bz2", "w")
a.write("this is a test of the emergency broadcast system")
del a

a = bz2.BZ2File("test5.bz2")
print a.read()
sys.exit(0)
# Compression
#

print "testing compress()"

print 'BZIP2 COMPRESS'
print '\n'
print '=================================================='
print '=============== Original String =================='
print '==================================================', '\n'
print string, '\n'

