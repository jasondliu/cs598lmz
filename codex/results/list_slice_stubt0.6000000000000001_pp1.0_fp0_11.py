import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
for i in range(100000):
    s=str()
    if i%2:
        weakref.ref(s,callback)
    else:
        weakref.ref(s)
    lst.append(s)

#结果：
#  在循环中创建了100000个字符串，每个字符串都有一个弱引用
#  其中50,000个字符串有一个回调函数
#  在循环结束时，解释器会自动调用gc.collect()然后打印结果
#  每次运行结
