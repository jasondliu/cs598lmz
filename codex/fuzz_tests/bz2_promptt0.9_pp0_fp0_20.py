import bz2
# Test BZ2Decompressor for having a read1 method with a count argument
reader = bz2.BZ2Decompressor()
reader.read1()
reader.decompress(b'1', 1)
# Check that iteration works, that the read method is used, and that
# StopIteration is handled
reader = bz2.BZ2Decompressor()
for line in reader:
    pass
reader = bz2.BZ2Decompressor()
reader.decompress(b'\r\n')
