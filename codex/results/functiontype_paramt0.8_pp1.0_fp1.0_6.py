from types import FunctionType
list(FunctionType('a',1,1,1))

#<a href="/A/B/C/../../../a.html">A</a>

#调整目录树
import os,sys

path = os.path.abspath(sys.argv[0]) #获得当前工作路径
path = os.path.split(os.path.dirname(path))[1]
path = os.path.split(os.path.dirname(os.path.abspath(path)))[1]
#print(path)

import os,sys

def changeDir():
	path = os.path.abspath(sys.argv[0]) #获得当前工作路径
	path = os.path.split(os.path.dirname(path))[1]
	path = os.path.split(os.path.dirname(os.path.abspath(path)))[1]
	return os.chdir(path)
