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
del keepali0e,lst,callback,A
#import time
#lst=[True]
#while lst:time.sleep(0.0000001)
#!del lst
#!import sys
#!sys.exit()
#@del lst
#@import sys
#@sys.exit()
#_del lst
#_import sys
#_sys.exit()

#!1L
#!1L[0]
#!1L[0][0]
#!1L[0][0][0]
#!1L[0][0][0][0]
#!1L[0][0][0][0][0]
#!1L[0][0][0][0][0][0]
#!1L[0][0][0][0][0][0][0]
#!1L[0][0][0][0][0][0][0][0]
#!1L[0][0][0][0][0][0][0][0][0]
#!1L[0][0][0][
