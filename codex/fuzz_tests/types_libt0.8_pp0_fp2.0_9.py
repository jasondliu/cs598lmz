import types
types.MethodType(func, obj)

# 2. 实例属性和类属性
class Person:
    name = 'Person'
p = Person()
p.name = 'chi'
# 优先使用实例属性，没有才会使用类属性
print(p.name)
del p.name
print(p.name)

# 3. 多重继承
class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass
# 打印class D的所有父类
print(D.__mro__)
print(D.mro())

# 4. 动态语言的特点
# 允许在程序运行时
