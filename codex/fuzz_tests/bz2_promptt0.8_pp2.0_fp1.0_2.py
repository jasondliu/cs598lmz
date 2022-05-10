import bz2
# Test BZ2Decompressor
bzdata = open('../../data/data.txt.bz2', 'rb').read()
decompressor = BZ2Decompressor()
try:
    data = decompressor.decompress(bzdata)
    print(data.decode())
except BZ2DecompressionError as e:
    print(e)

# Test BZ2File, 使用with语法
with BZ2File('../../data/data.txt.bz2', 'rb') as file:
    for line in file:
        print(line.decode())

# Test bz2.open()
with bz2.open('../../data/data.txt.bz2', 'rt', encoding='utf8') as file:
    for line in file:
        print(line)
