import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])


def run():
    t=str()
    while 1:
        t+=str()

lst=[]
for i in range(1024):
    lst.append(threading.Thread(target=run))
    lst[i].start()
for i in lst:
    i.join()

keepalive=[]
