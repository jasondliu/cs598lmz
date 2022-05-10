import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=weakref.ref(a,callback)
keepalive.append(lst)
del keepalive,a
del a,callback,lst,keepalive0
gc.collect()
print gc.collect()
</code>
I have tried this code in python 2.5 and 2.6, which both printed 0. But when I tried it in python 2.7, it printed 1, which means that the reference cycle is detected and destroyed.
I am just wondering why the behavior is different? 


A:

This is a known issue, CPython 2.x tries to detect reference cycles but the algorithm is flawed.
You can see the issue in action in the following transcript, where I run your code in Python 2.7.6:
<code>&gt;&gt;&gt; def run():
...     import gc
...     import weakref
...     class A(object):pass
...     def callback(x):del lst[0]
...     keepalive=[]
...     lst=[str()]
...     a
