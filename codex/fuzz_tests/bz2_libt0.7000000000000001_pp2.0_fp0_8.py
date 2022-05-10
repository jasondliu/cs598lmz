import bz2
bz2.BZ2File?

file = bz2.BZ2File("./data/00.bz2")
data = file.read()
print(data)

# bz2 是压缩文件，不是标准文件，所以不能被直接打开
# with open("./data/00.bz2") as f:
#     data = f.read()

# 跟 gzip 不一样， bz2 只能压缩一个文件，不能压缩多个文件

# bz2 可以压缩文件，但是不能压缩文件夹
# 如果要压缩文件夹，要么 zip，要么 tar
#
