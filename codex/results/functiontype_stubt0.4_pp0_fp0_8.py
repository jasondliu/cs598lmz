from types import FunctionType
a = (x for x in [1])
b = [1,2,3]
c = {'a':1,'b':2}
d = FunctionType
print(isinstance(a,Iterator))
print(isinstance(b,Iterator))
print(isinstance(c,Iterator))
print(isinstance(d,Iterator))

print(isinstance(a,Iterable))
print(isinstance(b,Iterable))
print(isinstance(c,Iterable))
print(isinstance(d,Iterable))

# 小结：
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict
