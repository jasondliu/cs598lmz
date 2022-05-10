import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

"""
函数说明:读取文件内容，并去重

Parameters:
    无
Returns:
    无
Author:
    Jack Cui
Blog:
    http://blog.csdn.net/c406495762
"""
def readFile():
    #打开文件
    file = open("data/data.txt","r")
    content_lines = file.readlines()  #读取所有行
    file.close()   #关闭文件
    #去重
    content_lines = list(set(content_lines))
    for i in range(len(content_lines)):
        content_lines[i] = content_lines[i].strip('\n')
    return content_lines

"""
函数说明:读取中
