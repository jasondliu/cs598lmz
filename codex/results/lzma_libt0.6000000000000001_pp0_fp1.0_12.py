import lzma
lzma.open(fn,'r',format=lzma.FORMAT_XZ)
with lzma.open(fn,'r',format=lzma.FORMAT_XZ) as f:
    print(f.read())

# 打开二进制文件，读取每个字节
with open(fn,'rb') as f:
    print(f.read())

# 打开文本文件，读取每个字符
with open(fn,'r',encoding='utf-8') as f:
    print(f.read())

# 打开文本文件，读取每行
with open(fn,'r',encoding='utf-8') as f:
    print(f.readlines())

# 打开文本文件，读取每行
with open(
