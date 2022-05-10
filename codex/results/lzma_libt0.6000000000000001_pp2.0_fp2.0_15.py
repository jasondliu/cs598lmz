import lzma
lzma.decompress(data)

# 解压失败，使用下面的方法
with open('data.xz', 'rb') as f:
    file_content = f.read()

# 其中：
# 1. file_content[:4]是magic number，解压时需要去掉，所以用file_content[4:]
# 2. format=lzma.FORMAT_ALONE表示单文件格式，即除去magic number后的数据就是要解压的数据
# 3. filters=[{"id": lzma.FILTER_DELTA, "dist": 1}]的意思是使用delta过滤器，见https://www.cnblogs.com/linxiyue/p/948
