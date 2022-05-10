import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#['']

#这个例子中，a的弱引用被放在keepalive中，a的c属性指向a自身，所以a不会被回收，
# 但是a的弱引用被回收了，所以回调函数被调用，lst中的字符串被删除，
# 所以lst中只剩下一个空字符串，所以打印出来的是['']

#这个例子中，a的弱引用被放在keepalive中
