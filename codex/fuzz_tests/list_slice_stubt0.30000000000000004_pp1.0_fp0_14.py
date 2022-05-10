import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
lst.append(weakref.ref(lst,callback))
del lst
gc.collect()
print(keepalive)

#列表推导式
#列表推导式是一个表达式，它会生成一个列表。它的语法与列表解析类似，但是它的操作更加灵活。
#列表推导式的语法是： [ expression for item in iterable (if condition) ]
#列表推导式可以接受多个 for 子句，如果接受多个 for 子句，则它们
