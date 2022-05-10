import types
types.FunctionType

def fun():
    pass

print(type(fun))
print(type(lambda x:x))
print(type(abs))
print(type(int))

#判断类型
a = 'abc'
print(isinstance(a,str))
print(isinstance(a,(str,int)))

#dir()函数
print(dir('abc'))

print('abc'.__len__())

#getattr() 和 setattr()
class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(getattr(obj, 'x'))
print(obj.x)
print(getattr(obj, 'y', 404))

#setattr(obj, 'y', 19)
#print(hasattr(obj, 'y'))
#print(getattr(obj, 'y'))

