import io
# Test io.RawIOBase().tell()

# create a raw file
f = io.FileIO("RawIOBase_tell.txt", "w+b")
print f

# read/write some data
#f.write(b"some data")
buf = bytearray(10)
n = f.readinto(buf)
print buf, n
#f.write(buf)
# seek to the beginning
#f.seek(0)
# read the whole file
b = f.read()
print 'b', b
# close the file
f.close()

# make sure the file is closed
#assert f.closed

#assert b == b"some data"
