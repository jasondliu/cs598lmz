import bz2
# Test BZ2Decompressor

file = bz2.BZ2File('data/sample.txt.bz2')
print(file.read())

file = bz2.BZ2File('data/sample.txt.bz2')
print(file.readline())

file = bz2.BZ2File('data/sample.txt.bz2')
print(file.readlines())

file = bz2.BZ2File('data/sample.txt.bz2')
for line in file:
    print(line)

file = bz2.BZ2File('data/sample.txt.bz2')
for line in file:
    print(line)
print(file.readlines())

file = bz2.BZ2File('data/sample.txt.bz2')
print(file.read())
print(file.readlines())

file = bz2.BZ2File('data/sample.txt.bz2')
print(file.read(10))
print(file.read(20))

file = bz2
