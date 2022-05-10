import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
callback(a)
a.c=a
callback(a)
a.c=a
callback(a)
del a,callback
print('collecting...')
sys.settrace(trace)
gc.collect()
try:
    print('running...')
    sys.gettrace()
except TypeError as e:
    print(e)
del lst
print(gc.collect())
