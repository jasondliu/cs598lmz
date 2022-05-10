import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(str())
del keepali0e
import gc
gc.collect() 
print(a)
'''
'''9
import weakref
def callback(x):
    print('callback')
    del frames[0]

def not_callback(x):
    pass

def print_frame():
    frames.append(x)

frames=[]
x=True
ref=weakref.ref(x,callback)
frames.append(x)
x=None
print_frame()
print(frames)
frames[0]=True
frames[0]=False
'''
'''10
def f(x):
    print('f')
    lst.append(x)

def print_frame():
    lst.append(x)

def g():
    print('g')

lst=[]
lst.append(f)
x=f
g()
print_frame()

print(lst)

'''
'''11
d={}
x=1
d[x]=True

