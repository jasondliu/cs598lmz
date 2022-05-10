from types import FunctionType
list(FunctionType('','','','',''))

#all() 判断一个可迭代对象是否全部都是True,如果有一个为False,则为False
#any() 判断一个可迭代对象是否存在为True的元素,只要有一个为True,则为True

#列表推导式
#写法:
#举例:取出列表中所有偶数
numbers = [1,2,3,4,5,6,7,8,9,10]
[x for x in numbers if x % 2 == 0]
#遍历字典
dic = {'name':'zhangsan','age':18}
[(k,v) for k,v in dic.items()]

#生成
