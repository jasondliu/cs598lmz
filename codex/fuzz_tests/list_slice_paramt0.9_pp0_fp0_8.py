import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(lst,callback))
del a
print lst
#now close the interpreter so that everything is garbage collected
#now run the command to do garbage collection and then examine lst
#open command prompt
#C:\Python26>python.exe -m gc
#output is 0
#C:\Python26>python.exe
#>>> from gc_test import lst
#>>> len(lst)
#1

#weakref.finalize
import resource
class Record(object):
def __init__(self):
self.value=42
print('creating the record object',self.value)
def __del__(self):
print('deleting the record object',self.value)
r=Record()
#creating the record object 42
weakref.finalize(r,print,'finalized with value',r.value)
del r
resource.getrlimit(resource.RLIMIT_DATA)[1]
#7218944
r=Record()
r.value=1e10 #out of memory
#finalized with value 100000000000.0

class Resource(object):

