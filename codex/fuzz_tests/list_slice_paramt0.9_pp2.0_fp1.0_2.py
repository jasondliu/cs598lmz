import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
x=1
lst[0]=a
lst[0]

print("--------第四题-------")
from time import time, sleep
def bar(fn):
    def wrap():
        start = time()
        fn()
        end = time()
        print("%s执行了%s" % (fn.__name__, end-start))
        return fn
    return wrap

@bar
def test1():
    for i in range(3):
        sleep(1)
        print('zhengze....')
        return test1
test1()
