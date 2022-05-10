import io
class File(io.RawIOBase):
	def write(self, b):
		return len(b)
f = File()
f.write(b'abcabcabc')


##与此相反，在大多数情况下，os模块不需要显式关闭. 要创建一个文件对象，使用 open() 函数:f = open(filename, mode)

import os
os.listdir(os.getcwd())

f = open('text.txt')
f.close()
## 生成一些文件名,
## 测试各种错误条件, 
## 打印一些调试信息, 
## 最后关闭。
## 如果不用 try...finally 这个代码
