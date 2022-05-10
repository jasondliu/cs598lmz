import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print sys.modules
#观察指向的地址发现，gc模块只管理a属性，而a属性指向a本身
#因此只要删掉属性a，a就能被正常回收。
del a
print lst
#print sys.modules

#a=A()
#b=A()
#a.c=b
#b.c=a
#lst=[str()]
#keepali0e.append(weakref.ref(a,callback))
#print sys.modules
#del a
#print lst
