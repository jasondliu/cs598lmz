import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
lst[0]=a
del a
del keepali0e
def f():
    for i in range(1000):
        str()
    del lst[0]
f()
</code>
If I run this code in Pycharm, it does not create any memory leak, but if I run this code in command line, it creates huge memory leak. 
In Pycharm, it prints:
<code>"C:\Program Files (x86)\Python36-32\python.exe" C:/Users/ycn/PycharmProjects/untitled/Memory Leak Weakref.py
0
0
0
0
0
0
0
0
0
0
</code>
But in command line, it prints:
<code>C:\Users\ycn\PycharmProjects\untitled&gt;"C:\Program Files (x86)\Python36-32\python.exe" Memory Leak Weakref.py
0
0
0
0
0
0
0
0
