from types import FunctionType
a = (x for x in [1])
b = [1]
c = {1}
d = {1:1}
e = FunctionType
f = 1
g = '1'
print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance(c, Iterator))
print(isinstance(d, Iterator))
print(isinstance(e, Iterator))
print(isinstance(f, Iterator))
print(isinstance(g, Iterator))

# 迭代器有两个基本的方法：iter() 和 next()。
#
# 字符串，列表或元组对象都可用于创建迭代器：
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

