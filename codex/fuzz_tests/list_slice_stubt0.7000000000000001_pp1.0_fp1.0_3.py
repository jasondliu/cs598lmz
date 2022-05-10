import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
del keepalive
lst[0]=weakref.ref(lst,callback)
del lst
import gc
gc.collect()
print "Finished"

#输出结果
#C:\Program Files\Python27\python.exe C:/Users/Administrator/PycharmProjects/Python_Study/Python_Study_Day04/day04_cycle_reference/test.py
#Finished
#
#Process finished with exit code 0
