import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=lst
a.e=keepali0e
keepali0e.append(weakref.ref(a,callback))
print(keepali0e)
keepali0e.append(lst)
keepali0e.append(keepali0e)
print(keepali0e)
del keepali0e
del a
del lst

import gc
collecteD_objects=gc.collect()
print('Collect %d.'%collecteD_objects,'Unreachable objects:%.3f'%unreachable_objects)
a=['a','b','c']
b=['1','2','3']
for i,j in zip(a,b):print(i,j)

def new_func(func):
	def wrap(x):
		print(x)
		return func(x)
	return wrap
def func(x):
	print(x+1)
func=new_func(func)
func(1)

def dec(func):
	def wrap(x):
		print(x)

