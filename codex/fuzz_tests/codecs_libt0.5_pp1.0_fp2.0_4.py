import codecs
codecs.open('/home/yfang/Downloads/test.txt', 'r', encoding='utf-8')

# 打开文件
f = open('/home/yfang/Downloads/test.txt', 'r')

# 读取文件
f.read()

# 关闭文件
f.close()

# 打开文件
f = open('/home/yfang/Downloads/test.txt', 'r')

# 读取文件
f.readline()

# 关闭文件
f.close()

# 打开文件
f = open('/home/yfang/Downloads/test.txt', 'r')

# 读取文件
for line in f.readlines():
    print(line)

# 关闭文件
f.close()

# 打开文件
f
