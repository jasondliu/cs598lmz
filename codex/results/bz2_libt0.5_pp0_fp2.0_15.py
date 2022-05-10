import bz2
bz2.BZ2File(path, "w")

# Compress data iteratively
with bz2.BZ2File(path, "w") as f:
    for line in data:
        f.write(line)

# Read the compressed file
with bz2.BZ2File(path, "r") as f:
    file_content = f.read()

# Decompress data
decompressed_data = bz2.decompress(file_content)

# END
