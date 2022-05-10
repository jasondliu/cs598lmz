import bz2
# Test BZ2Decompressor and BZ2Compressor
# BZ2Decompressor and BZ2Compressor are read-only file-like object
# They must be plugged into a stream for example io.BufferedReader or io.BufferedWriter

# BytesIO is an in-memory stream
mem_stream = io.BytesIO(b"this is a line")
with bz2.open(mem_stream, mode="wt") as f:
    f.write("this is a line")
    f.close()
    # Let's compress the line
print(mem_stream.getvalue())
# b'this is a line'

# Let's read the compressed line
mem_stream = io.BytesIO(b"this is a line")
with bz2.open(mem_stream, mode="rt") as f:
    print(f.readline())
    f.close()
    # Let's compress the line
# this is a line
