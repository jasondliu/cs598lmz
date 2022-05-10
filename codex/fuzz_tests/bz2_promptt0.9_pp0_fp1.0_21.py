import bz2
# Test BZ2Decompressor stream
file = open("python_tutorial.html.bz2", 'rb')
decompressor = bz2.BZ2Decompressor()
for data in iter(lambda : file.read(100 * 1024), b''):
    next_chunk = decompressor.decompress(data)
    if next_chunk:
        print("Text:", next_chunk.decode("utf-8"))
    else:
        print("waiting for more decompressed text")

print("Done")
file.close()

# Same as above but with file complete in one go
file = open("python_tutorial.html.bz2", 'rb')
compressed = file.read()
file.close()
comp_file = bz2.BZ2File("python_tutorial.html.bz2")
print("Original size:", len(compressed))
print("Read directly:", end=" ")
infile_comp_data = bz2.decompress(compressed)
print(len(infile_comp_data))
text = infile_comp
