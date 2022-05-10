import lzma
lzma.open

# lzma.open(filename, mode="r", format=None, check=-1, preset=None, filters=None)
# filename: 文件名
# mode: 打开模式
# format: 文件格式
# check: 校验和
# preset: 预设压缩级别
# filters: 压缩过滤器

# 压缩文件
with lzma.open("test.xz", "w") as f:
    f.write(b"hello world!\n")

# 解压文件
with lzma.open("test.xz") as f:
    file_content = f.read()
    print(file_content)

# 压缩文件
