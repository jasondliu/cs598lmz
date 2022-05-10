import codecs
codecs.open('1.txt','r','utf-8')

# 读取到内存，一次性读取
f = codecs.open('1.txt','r','utf-8')
# print f.read()

# 将文件分段读取到内存
f.read(1)
f.read(5)
f.read(10)

# 循环读取
for i in f:
    print i

# 文件内容的替换
f = codecs.open('1.txt','r','utf-8')
for i in f:
    if 'is' in i:
        print i.replace('is','are')

# 文件的写入
f = codecs.open('2.txt','w','utf-8')
f.write("我是李四")
f.close()

# 在文
