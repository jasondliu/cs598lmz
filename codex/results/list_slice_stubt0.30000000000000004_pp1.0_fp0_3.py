import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
lst

#这个程序的意思是，当删除a的时候，就会调用callback函数，callback函数的意思是删除lst的第一个元素，
#但是这里的lst[0]是一个空字符串，所以删除的时候没有任何影响，但是当删除a的时候，
#a.c=a，所以a.c也会被删除，但是a.c也是一个弱引用，
