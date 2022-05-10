import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=lst
print(lst)
del a
# print(lst)
gc.collect()
print(len(lst))

"""
2. 引用对象引用自身
除非引用对象引用自身，否则不会会造成循环引用
"""

# 无法释放循环引用
l=[]
l.append(l)
del l

# 引用自身
class A(object):pass
a=A()
a.c=a
del a

# 引用不自身
class A(object):pass
a=A()
b=A()
a.c=b
del a
del b


"""
3. 引用计数
