import lzma
lzma.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# 一个字节一个字节的读取
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    while data:
        print(data)
        data = f.read(16)

# 在文本文件上进行迭代
with open('somefile.txt', 'rt') as f:
    for line in f:
        print(line)

# 在二进制文件上进行迭代
with open('somefile.bin', 'rb') as f:
    while True:
        chunk = f.read(16)
        if chunk:
            process_data(
