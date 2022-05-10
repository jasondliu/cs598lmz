import codecs
codecs.open('test.txt','r','utf-8')

'''

# 文件复制
'''
# read 一次读取文件全部内容
with open('test.txt','r') as fr:
    re=fr.read()
    with open('test1.txt','w') as fw:
        fw.write(re)
# readline 读取一行数据
with open('test.txt','r') as fr:
    re=fr.readline()
    with open('test2.txt','w') as fw:
        fw.write(re)
#readlines 读取一行数据，返回一个列表
with open('test.txt','r') as fr:
    re=fr.readlines()
    with open('test3.txt','w') as fw:
        fw.write(re)
'''

# 换行
