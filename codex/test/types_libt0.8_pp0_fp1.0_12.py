import types
types.ClassType

# 定义一个类
class Hello(object):
    # self代表类的实例，而非类
    def hello(self, name='world'):
        print('Hello, %s.' % name)

# 实例化类
h = Hello()
print(type(Hello))
print(type(h))
print(type(type(Hello)))
# 调用hello方法
h.hello()

# 判断实例是否是某个类型
print(isinstance(h, Hello))

# 判断是否是一个类
print(isinstance(Hello, type))
# 判断一个对象是否是函数
print(isinstance(Hello, types.FunctionType))
