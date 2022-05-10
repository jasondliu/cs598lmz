import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
while keepali0e:sleep(0.1)
print lst
'''
This test will only work if the generator is recursively traversed depth first.
'''

import sys
if sys.version[:3]<'2.6':
	print 'This test requires Python 2.6 or later. Just assume that everything works.'
	sys.exit(0)

import weakref
class i(object):
	def __iter__(self): return self
	def next(self):raise StopIteration
	def __del__(self):
		print 'i died'
class A(list):
	pass
def callback(x):
	print 'callback'
d=[1,2,i(),3]
a=A(d)
b=A(d)
c=A(a)
c.append(b)
w=weakref.ref(a)
w2=weakref.ref(b,callback)
del a
del b
del d
w=w()

if w is not None:
	for i in w:pass
