import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
weakref.ref(a,callback)
keepalive.append(a)
del a
gc.collect()
print('a'*100,lst)
keepalive.append(lst)
del keepali0e,lst
gc.collect()
print('b'*100,lst)
#C:\Users\yang\Desktop\python\leetcode>python -m timeit -n 1000 -s "import gc,weakref,test" "test.callback(1)"
#1000 loops, best of 5: 2.73 usec per loop
#C:\Users\yang\Desktop\python\leetcode>python -m timeit -n 1000 -s "import gc,weakref,test" "test.callback(1)"
#1000 loops, best of 5: 2.72 usec per loop
#C:\Users\yang\Desktop\python\leetcode>python -m timeit -n 1000 -s "import gc,weakref,test" "test.callback(1)"
#1000 loops, best of 5: 2.73 usec per loop
