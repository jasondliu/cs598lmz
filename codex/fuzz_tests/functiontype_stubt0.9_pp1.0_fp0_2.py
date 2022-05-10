from types import FunctionType
a = (x for x in [1])
type(a)
#generator
#一个函数中只要有yield字符出现 就是一个generator的函数

#generator对异步处理极大的支持
#generator的执行过程
#1.next和send方法
#2.yield是个特殊的retrn
#3.yield from
#协程
#3个区别
#1.调用方send None
#2.子生成器 send过来得值会与yield expression表达式进行比较
#3.send会激活子生成器向外返回结果

#asyncio 生成器不能和as
