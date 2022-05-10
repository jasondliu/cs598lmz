import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.proxy(a))
print [id(x) for x in keepali0e]
'''
#print lst
#print weakref.ref(lst[0],callback)
#print lst
'''
for c in (1,2):
    print c
    if c>2:
        print 3
else:
    print 4
'''
'''
#encoding=utf-8
import os
print os.getcwd()
#raw_input('\n Press Enter to exit...')
'''
print range(10)[6:0:-2]
