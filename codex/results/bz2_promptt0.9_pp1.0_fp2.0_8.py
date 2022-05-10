import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()

compressed_lines = []
original_lines = []
compressed_size = 0
i=0
with open("data/example.json.bz2") as file_:
    while True:
        line = file_.readline()
        i+=1
        if line == '':
            break
        if (len(line) >= 24):
            decompressed_data = d.decompress(line).decode("utf-8")
            original_lines.append(decompressed_data)
            compressed_lines.append(line)
            compressed_size += len(line)
print("Read a total of {} uncompressed lines from the bz2 file".format(i))
print("Read a total of {} compressed lines from the bz2 file".format(len(compressed_lines)))
print("Compressed size: {}".format(compressed_size))

# Test GzipDecompressor
d = zlib.GzipDecompressor()

compressed_lines = []
original_lines = []
compressed_
