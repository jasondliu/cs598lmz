import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
data = decompressor.decompress(bz2_data)
data.decode('utf-8')

# Test BZ2File
with bz2.BZ2File(bz2_path) as f:
    data = f.read()
data.decode('utf-8')

# Test BZ2File with context manager
with bz2.BZ2File(bz2_path) as f:
    for line in f:
        print(line.strip().decode('utf-8'))

# Test BZ2File with readlines()
with bz2.BZ2File(bz2_path) as f:
    data = f.readlines()
for line in data:
    print(line.strip().decode('utf-8'))

# Test BZ2File with readline()
with bz2.BZ2File(bz2_path) as f:
    while True:
        line = f.readline()
        if not line
