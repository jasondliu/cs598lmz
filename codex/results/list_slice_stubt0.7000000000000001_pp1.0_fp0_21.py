import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
#keepalive.append(weakref.ref(lst[0],callback))
print("len(keepalive)={0}".format(len(keepalive)))
print("len(lst)={0}".format(len(lst)))
print("lst[0] is None?{0}".format(lst[0] is None))
print("del a")
del a
print("len(keepalive)={0}".format(len(keepalive)))
print("len(lst)={0}".format(len(lst)))
print("lst[0] is None?{0}".format(lst[0] is None))
print("del lst[0]")
del lst[0]
print("len(keepalive)={0}".format(len(keepalive)))
print("len(lst)={0}".format(len(lst)))
print("lst[0] is None?{0}".format(lst[0] is
