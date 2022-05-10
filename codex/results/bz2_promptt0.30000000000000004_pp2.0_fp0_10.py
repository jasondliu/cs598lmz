import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed)

# Decompress the entire file
with bz2.open("data.bz2", "rb") as f:
    file_content = f.read()

# Read the file line by line
with bz2.open("data.bz2", "rt") as f:
    for line in f:
        print(line)

# Compress a file
with open("data.txt", "rb") as f_in:
    with bz2.open("data.bz2", "wb") as f_out:
        f_out.writelines(f_in)
