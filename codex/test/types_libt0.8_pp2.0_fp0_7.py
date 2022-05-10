import types
types.MethodType(instancemethod(cmp,None,list),list)

# 人类
class Person(object):
    # 属性
    age = 0
    # 构造函数
    def __init__(self,age=0):
        self.age = age
    # 实例方法
