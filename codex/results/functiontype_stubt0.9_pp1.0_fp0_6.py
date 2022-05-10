from types import FunctionType
a = (x for x in [1]) 
print(type(a), type(a) == GeneratorType)

b = (x for x in [1]) 
def c(func):
    return func
print(type(c), type(c) == FunctionType)


from json import dumps as json_dumps
#模块是自己定义
from json import *
from json.encoder import *
from json.encoder import encode_basestring as cbs
json_dumps = json_dumps

import json
print(type(json.dumps), type(json.dumps) == FunctionType)

#----------------------------------

#python 伪私有变量:在变量名前面加上两个下划线 

class C:
    def __init__(self):
        self.__x = 1
    def getx(self):
        return self.__x

c = C()
print(c.getx())


#python 中的
