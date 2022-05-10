import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
r=weakref.ref(a.c,callback)
del a
for i in range(int(1e6)):
    l=lst[:]
    l.append(l)
    l.append(lst)
    keepalive.append(l)
import gc
del keepalive
gc.disable()
gc.collect()

##ERROR:
#x=object.__new__(str)
##TypeError: str.__new__(str): not enough arguments
##ERROR:
x=str.__new__(str)
#TypeError: str.__new__(str): not enough arguments
#ERROR:
x=str()
#TypeError: str.__new__(str): not enough arguments
print str,str(),str(unicode)
#<type 'str'>
#
#<type 'unicode'>
##ERROR:
#x=str(unicode(''),latin-1)
##TypeError: __init__() takes at most 2 arguments (3 given)
##ERROR:
#x=unicode(''),latin-
