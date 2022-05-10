import codecs
codecs.open('f:/myfile.txt','r','utf-8')
#打开文件并读取内容
with codecs.open('f:/myfile.txt','r','utf-8') as f:
    s=f.read()
    print(s)

#使用codecs写入文件
#写入到文件
with codecs.open('f:/myfile.txt', 'w', 'utf-8') as f:
    f.write('hello,world')
'''
练习
请读取一个文件，然后把内容写入到另一个文件中。
'''
with codecs.open('f:/myfile.txt','r','utf-8') as f:
    s=f.read()
with codecs.open('f:/myfile2.txt','w','utf-8') as f2:
    f2.
