import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]=a
del a
import gc
gc.collect()
print(lst)

print("========================================")

import threading
import time
def func():
    print("sub thread start")
    time.sleep(1)
    print("sub thread end")
t=threading.Thread(target=func)
t.start()
time.sleep(0.2)
print("main thread")


print("========================================")

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args
    def run(self):
        self.func(*self.args)

def loop(nloop,nsec):
    print("start loop ",nloop," at: ",time.ctime())
    time.sleep(nsec)
    print("loop",nloop,"done at: ",time.ctime())

def main():
    print("
