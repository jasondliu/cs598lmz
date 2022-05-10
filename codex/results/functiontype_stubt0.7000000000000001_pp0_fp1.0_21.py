from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])

print(a == b)  # False
print(a is b)  # False
print(a)  # <generator object <genexpr> at 0x000000000236AFC0>
print(a.__next__())  # 1

print(type(a.__next__))  # <class 'method-wrapper'>
print(type(a.__next__()) is int)  # True

print(type(a.__next__) is FunctionType)  # True

'''
练习
'''
# 请用生成器写一个简单的函数
# 当参数是数字时，返回该数字的所有约数
# 如：传入100，返回[1,2,4,5,10,20,25,50,100]

def get_yueshu(num
