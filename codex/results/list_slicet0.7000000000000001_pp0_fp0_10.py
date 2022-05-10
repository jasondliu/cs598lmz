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

#构造循环引用
class Graph(object):pass
def setup(obj):
    global lst
    lst=lst[:]+[obj]
    obj.c=lst[0]
lst=[Graph()]
setup(lst[0])
del lst
while lst:keepali0e.append(lst[:])

#构造自引用
lst=[str()]
lst.append(lst)
del lst
while lst:keepali0e.append(lst[:])

#构造树形引用
lst=[str()]
lst.append([lst,lst])
del lst
while lst:keepali0e.append(lst[:])

#构造混合引用
lst=[str()]
lst.append([lst,lst,[lst,lst]])
lst[0].append(l
