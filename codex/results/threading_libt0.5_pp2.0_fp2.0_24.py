import threading
threading.Thread(target = lambda: print('hello world')).start()

#线程传参
import threading
def f(a,b):
    print(a+b)
threading.Thread(target = f,args=(1,2)).start()

#线程传参
import threading
def f(a,b):
    print(a+b)
threading.Thread(target = f,kwargs={'a':1,'b':2}).start()

#线程传参
import threading
def f(a,b):
    print(a+b)
threading.Thread(target = f,args=(1,2),kwargs={'a':1,'b':2}).start()

#线程传参
import threading
def f(a,b):
    print(a+b)
threading.Thread(target = f,args=(1,2),kwargs={'a':1,'b':2}).start()

#
