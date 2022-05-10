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



#This is an example of how to create an infinite loop.
#This loops forever
import time
def loop():
    print "Loop started"
    while True:
        print "infinite loop"
        time.sleep(1) #sleep for one second
print "Calling loop"
loop()
print "Called loop" #This line of code will never be executed



#This is an example of how to create a recursive infinite loop.
#This loops forever
import time
def loop():
    print "Loop started"
    loop()
print "Calling loop"
loop()
print "Called loop" #This line of code will never be executed



#This is an example of python code which will infinite, the reason is the main module,
#when the while loop over, the delete all the object, but still keep the reference alive.
#So the callback will get called, and remove the last reference of lst, del lst[0]
#This is also an infinite loop.
#This loops forever
import weakref
def callback(x):del lst[0]
keepali0e=[]
