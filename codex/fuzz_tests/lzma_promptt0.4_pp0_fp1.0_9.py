import lzma
# Test LZMADecompressor

with lzma.open("/home/carlos/Downloads/enwik9") as f:
    file_content = f.read()
    print(file_content[:100])

# Test LZMACompressor

with lzma.open("/home/carlos/Downloads/enwik9.xz", "w") as f:
    f.write(file_content)

print("Done")

# Test LZMADecompressor

with lzma.open("/home/carlos/Downloads/enwik9.xz") as f:
    file_content = f.read()
    print(file_content[:100])

print("Done")

# Test LZMAFile

with lzma.open("/home/carlos/Downloads/enwik9.xz") as f:
    file_content = f.read()
    print(file_content[:100])

print("Done")

# Test LZMAFile

with lzma.open("/home/c
