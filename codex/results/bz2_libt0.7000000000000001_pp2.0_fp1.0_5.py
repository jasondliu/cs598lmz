import bz2
bz2_file = bz2.BZ2File('data.json.bz2')
for line in bz2_file:
    print(line)

# 停止与bz2文件的交互
bz2_file.close()

# 对于压缩的文件，一般来讲，需要使用with语句来确保文件会被关闭
with bz2.BZ2File('data.json.bz2') as bz2_file:
    for line in bz2_file:
        print(line)

# 此外，压缩打开的文件还有一个read方法，可以一次性返回文件中所有的内容
with bz2.BZ2File('data.
