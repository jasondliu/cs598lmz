import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
print(lst)
lst[0]="test"
lst[0]="test"
print(lst)
print(w())
print(w())
keepalive[0].c=None
print(w())
print(w())
print(w())
print(lst)
del keepalive[0]
print(w())
print(lst)

#构造函数
def ref(ob,callback=None):
    return weakref.ref(ob,callback)
ref('test')

#弱引用
class A(object):pass
def callback(x):print("callback:",x)
keepalive=[]
lst=[str()]
a=A()
keepalive.append(a)
w=ref(a,callback)
del a
print(w())
print(w())
print(w())
print(w())
del keepalive[0]
print(w())

