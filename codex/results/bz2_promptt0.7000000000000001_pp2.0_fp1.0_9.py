import bz2
# Test BZ2Decompressor
with open('data/random.txt.bz2', 'rb') as f, bz2.BZ2Decompressor() as decomp:
    for block in iter(lambda : f.read(100), b''):
        print(decomp.decompress(block))

print()

# Test BZ2File
with bz2.BZ2File('data/random.txt.bz2') as file_:
    print(file_.read())

print()

# Test BZ2File with mode 'w'
value = b'This is a test of the bz2 module.\n'
with bz2.BZ2File('data/random.txt.bz2', 'w') as file_:
    file_.write(value)

print()

# Test BZ2File with mode 'rt'
with bz2.BZ2File('data/random.txt.bz2', 'rt') as file_:
    print(file_.read())

print()

# Test BZ2File with mode 'wt'
text = '
