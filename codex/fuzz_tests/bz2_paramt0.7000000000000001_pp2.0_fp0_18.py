from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(access_log_compressed)

# now we can open the file!
f = open(access_log_compressed.name) 
print(f.read())
f.close()

# cleanup
os.remove(access_log_compressed.name)

# REVIEW: What is the difference between bz2.BZ2Decompressor
# and bz2.BZ2File?

# BZ2Decompressor() is a function that takes a compressed file object
# and decompresses it. The file object must support read() and close()
# which gzip.GzipFile does.

# BZ2File() is a class that opens a compressed file and decompresses it
# on the fly. It also supports write() to compress data as you write it.
# It does not support random access, so you can't seek backwards and
# read data you previously read.


# EXERCISE: Create a BZ2File object using BZ2File() and read
# the access log from it.





# EXERCISE: Decompress the access log file
