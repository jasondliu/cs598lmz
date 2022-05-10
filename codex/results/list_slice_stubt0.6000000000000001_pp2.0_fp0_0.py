import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a.c
a.a=a.b
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(a.b)
keepali0e.append(a.a)
keepali0e.append(str())
a.a=str()
a.b=str()
a.c=str()
a=str()
keepali0e.append(lst)
keepali0e.append(callback)
del keepali0e
lst[0]="a"*(2**31-1)
gc.collect()
del lst
print('ok')

# 在 32 位 Python 中，会触发一个段错误，在 64 位 Python 中，会触发一个内存溢出错误。
# 在 32 位 Python 中，系统假
