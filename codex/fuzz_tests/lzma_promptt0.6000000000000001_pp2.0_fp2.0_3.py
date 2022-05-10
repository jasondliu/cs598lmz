import lzma
# Test LZMADecompressor
with open("decompressed.txt", "wb") as outfile:
    with lzma.open("compressed.txt.xz") as infile:
        for line in infile:
            outfile.write(line)
 
# Test LZMACompressor
with lzma.open("compressed.txt.xz", "w") as outfile:
    with open("decompressed.txt", "rb") as infile:
        outfile.write(infile.read())
 
# Verify that the compressed file works
with open("decompressed2.txt", "wb") as outfile:
    with lzma.open("compressed.txt.xz") as infile:
        for line in infile:
            outfile.write(line)
 
# Verify that the two decompressed files match
with open("decompressed.txt", "rb") as f1, open("decompressed2.txt", "rb") as f2:
    assert f1.read() == f2.read()


# LZMADecompressor
# decomp
