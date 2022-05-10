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
