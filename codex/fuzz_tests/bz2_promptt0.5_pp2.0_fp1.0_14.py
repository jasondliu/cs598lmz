import bz2
# Test BZ2Decompressor

with bz2.BZ2File("enwik8.bz2", 'r') as f:
    decomp = bz2.BZ2Decompressor()
    for chunk in iter(lambda: f.read(100 * 1024), b''):
        data = decomp.decompress(chunk)
        if data:
            print(data)
            break

print("Done")

# Test BZ2File

with bz2.BZ2File("enwik8.bz2", 'r') as f:
    for line in f:
        print(line)
        break

print("Done")

# Test BZ2File with decompressor

with bz2.BZ2File("enwik8.bz2", 'r') as f:
    decomp = bz2.BZ2Decompressor()
    for line in f:
        print(line)
        break

print("Done")

# Test BZ2File.read()

with bz2.BZ2File("enwik8.bz2", '
