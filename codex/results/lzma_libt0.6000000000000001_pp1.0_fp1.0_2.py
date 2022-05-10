import lzma
lzma.open(file, mode="rt").read()

# 通过lzma.LZMAFile类可以访问其他模式
with lzma.open(file, mode="rt") as f:
    print(f.read())

with lzma.open(file, mode="rt", encoding="utf-8") as f:
    print(f.read())

with lzma.open(file, mode="rt", encoding="cp437") as f:
    print(f.read())

with lzma.open(file, mode="rt", encoding="utf-8", errors="ignore") as f:
    print(f.read())

with lzma.open(file, mode="rt", encoding="ascii", errors="surrogateescape") as f:
    print(f.read())

# 如果没有指定编码，在文本模式下
