import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c))
keepali0e.append(weakref.ref(a,callback))
del a
time.sleep(2)
print lst[0]

''' 测试 闭包
def add1(x):
    return x+1

def cal():  # 装饰器
    return add1(3)


print cal()

g = lambda x:x+1
print g(2)'''
def testclosure():
    fs=[]
    for i in range(1,4):
        fs.append(lambda:i*i)   ##闭包
    return fs
f1,f2,f3=testclosure()
print f1(),f2(),f3()

def testClosure1():
    fs=[]
    for i in range(1,4):
        def f():
            # i=i  **i**
            return i*i   ##闭包
        fs.append(f)
    return fs
f1,f2,f3=testClosure1()
