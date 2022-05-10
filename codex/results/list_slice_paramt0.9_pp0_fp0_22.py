import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0].replace(b'\xff',b'xx')
print (keepali0e)

#   假如a.c=a 说明a 放在可达性目录 它不在引用计数上面  等a 的引用计数为0 会把a 从 可达性目录移除  那么在移除不存在的引用回调函数  会出问题
