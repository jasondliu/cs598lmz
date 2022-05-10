import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
for i in range(40):print(len(lst))

# 参考答案
# lst=[]
# lst.append(str())
# lst.append(lst)
# del lst
# for i in range(40):
# 	print(len(lst))


# 为什么可以这样
a=[]
b=[a]
a.append(b)

# 为什么不可以这样
# a=[]
# b=[a]
# a=b

# 为什么可以这样
a=[]
b=[a]
a=b
a.append(b)

# 为什么不可以这样
# a=[]
# b=[a]
# a.append(b)
# a=b

# 为什么可
