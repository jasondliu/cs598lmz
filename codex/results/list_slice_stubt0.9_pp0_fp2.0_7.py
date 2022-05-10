import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(lst)
keepalive.append(a)
t1=threading.Thread(target=callback,args=(a,))
t2=threading.Thread(target=a.c)
t1.start();t2.start();t1.join();t2.join()
