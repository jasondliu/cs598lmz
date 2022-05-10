import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# 打开文件
# fo = open("foo.txt", "r+")
# print ("文件名: ", fo.name)

# 关闭文件
# fo.close()

# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("读取的字符串是 : ", str)

# 查找当前位置
position = fo.tell()
print ("当前文件位置 : ", position)

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(10)
print ("重新读取
