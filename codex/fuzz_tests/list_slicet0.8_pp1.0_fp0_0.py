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
</code>
Also, I would like to call a function after the object is deleted to clean up the resouces being used by the object. Would the following code do the job?
<code>import weakref
class A(object):
  def __init__(self, num):
    self.num=num
    self.openFile()
  def openFile(self):
    self.file=open('file'+str(self.num)+'.txt', 'w')
  def closeFile(self):
    self.file.close()
  def __del__(self):
    self.closeFile()
def callback(x):
  print 'Callback for', x.num
lst=[str()]
a=A(1)
keepali0e=[weakref.ref(a,callback)]
del a
while lst:keepali0e.append(lst[:])
del lst
</code>


A:

<code>sys.getrefcount</code> is not reliable. See Python: sys.getrefcount() is 2 higher than it should be
<blockquote
