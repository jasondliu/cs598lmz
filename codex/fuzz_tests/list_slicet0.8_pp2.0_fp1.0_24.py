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

#与多线程有关
import gc,pthread
global_list=[]
def worker():
    for i in xrange(10000000):
        global_list.append(str(i))
t=pthread.start_new_thread(worker,())
gc.enable()
gc.collect()
t.join()
print global_list
gc.collect()

#避免浅复制
import copy
a=[1,[2],3]
b=copy.deepcopy(a)

#使用变量名而不是数字索引使列表操作更容易理解
data=[(1,2),(3,4),(5,6)]
def func():
    for id,x in data:
        print x

#防御多线程
import threading
x=[0]
LOCK=threading.Lock()
def add_one():
    L
