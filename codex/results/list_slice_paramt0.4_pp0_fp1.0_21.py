import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
print(keepali0e)
print(keepali0e[0]())
print(lst)

#['']
#[<weakref at 0x000001E1D1F7B0B8; to 'A' at 0x000001E1D1F7B0D0>]
#<__main__.A object at 0x000001E1D1F7B0D0>
#[]
