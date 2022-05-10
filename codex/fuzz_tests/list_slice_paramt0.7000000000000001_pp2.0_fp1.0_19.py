import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
if __name__=='__main__':
    import gc
    gc.collect()
    print(len(lst))
    gc.collect()
    print(len(lst))
