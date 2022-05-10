import types
types.MethodType

# MethodType 用于给对象动态绑定方法

class A:
    pass


# 动态给类A绑定一个方法say
# 创建一个函数，函数名为say
def say(self):
    print('say')

# 通过types模块中的MethodType方法，绑定方法到类A中
# 第一个参数为方法，第二个为类名
a = A()
a.say = types.MethodType(say, A)
a.say()

# 动态给类A绑定一个类属性name
A.name = 'Tom'
print(A.name)

#
