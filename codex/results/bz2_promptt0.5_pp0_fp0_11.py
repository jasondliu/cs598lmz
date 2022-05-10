import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open("data/small.bz2", "rb") as input:
    with open("data/small.out", "wb") as output:
        decompressor.decompress(input.read(), output)
!cat data/small.out

# Test BZ2File

with bz2.BZ2File("data/small.bz2", "r") as input:
    with open("data/small.out2", "w") as output:
        output.write(input.read())

!cat data/small.out2
 
# Compress a file

with open("data/small.bz2", "wb") as output:
    with bz2.BZ2File("data/small.bz2", "w", compresslevel=9) as bz_output:
        output.write(bz_output.read())
 
# Compress a string

compressed = bz2.compress("This is a string")

print(compressed)


