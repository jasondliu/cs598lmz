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

#结果:['<__main__.A object at 0x0000000003E4F4A8>']
#引用了A对象的字符串表示形式,没有调用回调函数

#例2
import weakref
class A(object):
    def __init__(self,x):
        self.x=x
    def __repr__(self):
        return str(self.x)
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A(1)
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#结果:['1']
#引用了A对象的字符串表示形式
