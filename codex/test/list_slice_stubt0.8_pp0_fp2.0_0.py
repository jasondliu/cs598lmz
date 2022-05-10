import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepali0e.append(a)
keepali0e.append(a.b)
keepali0e.append(a.c)
x=weakref.ref(a,callback)
del a
"""

struct1 = """
class Node(object):pass
class A(object):
	def __init__(self,lst):
		self.lst=lst
		self.childs=[]
		for i in lst:
			n=Node()
			self.childs.append(n)
			i.add(n)

def make(lst):
	for i in range(len(lst)-1):
		a=A(lst[i:i+2])

