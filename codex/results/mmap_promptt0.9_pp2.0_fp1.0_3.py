import mmap
# Test mmap.mmap
G = mmap.mmap ( 1, 1024, "gmmap", mmap.ACCESS_WRITE, "gmmap" )
G.seek ( 0 )
G.write ( "!" )
G.read ( len ( "!" ) )
