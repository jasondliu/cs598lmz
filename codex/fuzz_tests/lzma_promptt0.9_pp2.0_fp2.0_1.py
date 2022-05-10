import lzma
# Test LZMADecompressor

# decompress from file.txt.xz
with lzma.open("file.txt.xz", "r") as fp:
    content = fp.read()
    print("Content:", content)
    print("Number of  Bytes Read:", len(content))

# decompress from file.txt.xz
fp = lzma.LZMADecompressor()
with open("file.txt.xz", "rb") as fp2:
    content = fp.decompress(fp2.read())
    print("Number of  Bytes Read:", len(content))
    print("Content:", content)
 
print("---------------------")

# Error Handling

with lzma.open("file2.txt.xz", "r") as fp:
    content = fp.read()
    print("Content:", content)
    print("Number of  Bytes Read:", len(content))
    print("Decompressor:", fp.decompressor)
    while True:
        try:
            tmp = f
