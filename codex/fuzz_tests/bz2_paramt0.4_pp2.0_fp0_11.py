from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# To compress a string
bz2_comp = BZ2Compressor()
bz2_comp.compress(data)
bz2_comp.flush()

# To compress a file
with open('file.txt', 'rb') as input:
    with bz2.BZ2File('file.txt.bz2', 'wb') as output:
        output.writelines(input)

# To decompress a file
with bz2.BZ2File('file.txt.bz2', 'rb') as input:
    with open('file.txt', 'wb') as output:
        for line in input:
            output.write(line)
