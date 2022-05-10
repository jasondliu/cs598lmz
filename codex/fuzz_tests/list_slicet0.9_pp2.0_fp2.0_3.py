import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

# code 12
t=[[]]
for i in range(20):t+=t

# code 13
class Node(object):pass
def traversal(n):
  yield n
  for c in n.children:
    for x in traversal(c): 
      yield x
n=Node()
n.children=[n]
list(traversal(n))

# code 14
d={}
while True:
  d[d]=d

# code 15
func=lambda func:func(func)
func(func)

# code 16
try:
  raise "spam"
except:
  raise

# code 17
class Ta(object):
  def thing(self):eval("1 "*(10**6))
a=Ta()
raise a.thing()

# code 18
print('Recursion detected; deep recursion on default' if__name__=='__main__'else' deep recursion on default')

# code 19 
import threading,os
def f():threading.Thread(target=os.getpid, args=
