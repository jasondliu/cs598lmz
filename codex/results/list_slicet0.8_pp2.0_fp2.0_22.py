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

p11=0

g00=None

l2=0
l1=0
l4=None
l3=0

try:
  import sys
  import traceback
  def excepthook(exc_type,exc_value,tb):
    traceback.print_exception(exc_type,exc_value,tb)
    sys.exit(1)
  sys.excepthook=excepthook
except:
  pass

def badmalloc():
  l2=7
  l1=5
  l5=l2
  l6=l5
  l7=l6
  l8=l3
  l9=l7
  l10=l9
  l11=l10
  l12=l8
  l13=l11
  l14=l12
  l15=l13
  l16=l14
  l17=l15
  l18=l16
  l19=l17
  l20=l18
  l21=l19
 
