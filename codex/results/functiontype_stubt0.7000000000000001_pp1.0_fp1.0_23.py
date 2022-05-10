from types import FunctionType
a = (x for x in [1])
print(isinstance(a, FunctionType))
print(isinstance(lambda x:x, FunctionType))
print(isinstance(lambda x,y:x, FunctionType))

print("-------------")
class A:
    def __init__(self):
        self.a = 1

a = A()
delattr(a, 'a')
print(a.a)
try:
    #调用没有的属性会报错
    delattr(a, 'b')
except AttributeError as e:
    print(e)

print("-------------")
#callable 判断是否可以调用
print(callable(a))
print(callable(A))
print(callable(A.__init__))
print(callable(A.__init__.__call__))

print("-------------")
#compile 将字符串编译成代码对象
#compile(
