import io
# Test io.RawIOBase.seekable
infile = open(__file__, "r")
assert infile.seekable() == True
infile.close()
