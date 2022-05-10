import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(a)
b=A()
lst.append(b)
b.c=b
lst[1].c=lst[1]
del a
del b
lst[1].c=lst[1]
del lst[1].c
lst[0]=lst[0].replace('','')
lst[0]=lst[0].replace('','')
lst[0]=lst[0].replace('','')
def func():
    dic=globals()
    func=dic['func']
    dic['func']=None
    func()
func()
del dic['func']
del dic
del func
del sys
del keepalive
del weakref
del __builtins__
del callback
lst[0]=lst[0].replace('','')
lst[0]=lst[0].replace('','')
lst[0]=lst[0].replace('','')
a=A()
a.x
