from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))

'''
<generator object <genexpr> at 0x0000022A6A7C6F48>
<class 'generator'>
False
True
'''

'''
# 迭代器
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字
