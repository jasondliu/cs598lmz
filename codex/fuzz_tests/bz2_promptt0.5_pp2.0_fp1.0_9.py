import bz2
# Test BZ2Decompressor

# Read from file
bz2_file = bz2.BZ2File("../data/enwiki-latest-pages-articles1.xml-p10p30302.bz2", "r")
content = bz2_file.read()
bz2_file.close()

# Decompress
decompressor = bz2.BZ2Decompressor()
data = decompressor.decompress(content)

print(data)

# Write to file
with open("../data/enwiki-latest-pages-articles1.xml-p10p30302", "w") as f:
    f.write(data)

# Read from file
with open("../data/enwiki-latest-pages-articles1.xml-p10p30302", "r") as f:
    content = f.read()

print(content)

# Compress
compressor = bz2.BZ2Compressor()
data = compressor.compress(content)
data += compressor.flush()

print(data)

# Write to file
with
