import bz2
# Test BZ2Decompressor with a binary file
decompressor = bz2.BZ2Decompressor()
with open('data.bz2', 'rb') as file:
    data = file.read()
    try:
        while True:
            chunk = decompressor.decompress(data)
            if chunk:
                print(len(chunk))
                print(chunk)
            else:
                break
    except EOFError:
        pass

# Test BZ2Compressor with a binary file
compressor = bz2.BZ2Compressor()

with open('data.bz2', 'wb') as file:
    file.write(compressor.compress(data))
    file.write(compressor.flush())

# Test BZ2File with a text file
with bz2.BZ2File('data.bz2', 'w') as file:
    for i in range(10):
        print(i, file=file)

with bz2.BZ2File('data.bz2', 'r') as file:
    while True:
