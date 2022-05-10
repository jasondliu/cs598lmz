import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
keepalive.append(a)
info_dict=weakref.getweakrefcounts()
for k,v in info_dict.items():
    if info_dict[k]>1:
        print(k)
        print(v)
