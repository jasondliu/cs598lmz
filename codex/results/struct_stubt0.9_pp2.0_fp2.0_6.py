from _struct import Struct
s = Struct.__new__(Struct)

s.__setattr__('format','hhHlll')
print(s.size)
print(s.format)

#重写__new__方法，但维护__init__方法
class new_way(object):
    def __new__(self,a,b,c,d):
        return super().__new__(self)
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        print(a+b+c+d)
    def __getattribute__(self, name):
        return super().__getattr
#__new__方法的主要作用是给对象分配内存空间，而 __init__ 方法则用来执行对象初始化的操作
#这
