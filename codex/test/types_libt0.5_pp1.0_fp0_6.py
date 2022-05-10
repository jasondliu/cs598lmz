import types
types.MethodType(func, None, class1)

# 2.通过实例添加方法
class class2(object):
    pass

def func(self, name="world"):
    print("hello, %s" % name)

instance = class2()
instance.func = types.MethodType(func, instance)
instance.func()

# 3.通过类添加方法
class class3(object):
    pass

def func(self, name="world"):
    print("hello, %s" % name)

class3.func = func

instance = class3()
instance.func()

# 4.限制实例属性
class class4(object):
    __slots__ = ("name", "age")  # 用tuple定义允许绑定的属性名称

instance = class4()
instance.name = "yang"
instance
