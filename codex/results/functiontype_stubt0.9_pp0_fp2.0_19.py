from types import FunctionType
a = (x for x in [1])
type(a)

from decimal import Decimal
Decimal(1)
type(Decimal(1))

'''
(理论知识)(探究类型源码真相)

上面的实例中我们可以看到生成器类型是交互解释器的内置类型:
但是我们查看类型的源码去了解类型的实现原理.发现不是简单的类实现:

'''
print('''

类型是类的实例
----------------------------------------
types.GeneratorType 源码:
class GeneratorType(type):
    def __
