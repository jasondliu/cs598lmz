import lzma
# Test LZMADecompressor
with lzma.open("ondmarc-com_xxxxxxxx_xxxxxxxxxx_20190326075537.eml.lzma") as infile:
    for line in infile:
        print(line.decode().strip())
