from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__ = Struct.__dict__
class Enum(object):
    def __init__(self,y=1):
        self.x = (1,2,3)
        self.y = y

e = Enum(y=2)
e.x

e.x = (4,5,6)

e.x


for x in e.x:
    print x

x

getattr(e,'x')


a = 1
b = 2
c = 3
a,b,c



def func(a=1,b=2,c=3,z='test',d=4,*args,**kwargs):
    print 'in func',a,b,c,d,z
    print 'args',args
    print 'kwargs',kwargs
    return 'ok'

func()


s = func(a=1,b=2,c=3,z='test',d=4)

s = func(1,2,3,'test',d=4)


s = func(z
