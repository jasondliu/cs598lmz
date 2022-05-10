from types import FunctionType
a = (x for x in [1])
a.__name__

# 类的方法也是对象
def bar(self, name='world'):
    print('hello, %s' % name)


Hello = type('Hello', (object, ), dict(hello=bar))
h = Hello()
h.hello()
print(type(bar))
# output:
# <type 'function'>

# 要创建一个class对象，type()函数依次传入3个参数：

# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称
