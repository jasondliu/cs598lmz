import mmap
# Test mmap.mmap in read mode to see if the file exists and is > 0 bytes
f = open( 'mapfile.txt', 'w+')
f.write( 'asdf' )
f.seek( 0 )
m = mmap.mmap( f.fileno(), 0 )
