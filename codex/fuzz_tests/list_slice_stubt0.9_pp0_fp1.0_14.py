import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)

keepali0e=a
keepali0e=KeepAli0e()
keepali0e.network.AutoRunning=1

N=10000
lst=N*[lambda :0]
del lst
keepali0e.network.AutoRunning=1

@keepali0e.network.HandleAfter
def f(x):pass
def handler(t_fun,t_args:tuple,t_kwargs:dict):
    print(x)
for i in range(1,10):
    keepali0e.network[f](i,handler=handler)
#@keepali0e.network.HandleAfter
#def f(x):
#    print(x)
#for i in range(1,10):
#    keepali0e.network[f](i)
#
#@keepali0e.network.HandleAfter
#def g(x,y,z="Z",**kwargs):
#    print(x,",",y,",",z,",**kwargs=",
