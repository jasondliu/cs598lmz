import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
del a
del keepalive
gc.collect()
print lst

#第一次执行会打印：['']
#第二次执行会打印：['']
#第三次执行会打印：['']
#第四次执行会打印：['']
#第五次执行会打印：['']
#第六次执行会打印：['']
#第七次执行会打印：['']
#第八次执行会打印：['']
#第九次执行
