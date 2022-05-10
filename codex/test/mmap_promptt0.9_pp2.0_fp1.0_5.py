import mmap
# Test mmap.mmap
#A = array(shape=(7,1,12),typecode=Float32)
#  Dealing with binary data is a pain
#  when we use the mmap module we are dealing with C arrays.
#  A[] = P[:]
#  A = P[:]
#  P = A[:]
## Warning: The following statements return the values in the array
##  but modify (corrupt) the underlying binary data file
##  This is true of both the mmap module and the array module
##  So I had to open the file in read-only mode.
#P = mmap.mmap(outfd.fileno(),0,access=mmap.ACCESS_COPY)
#P[:] = A[:]
#A = P[:]
# Here's a test
