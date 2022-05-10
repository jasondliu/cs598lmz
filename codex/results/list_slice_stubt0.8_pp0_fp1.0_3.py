import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a # make A cycle
keepalive0=weakref.ref(a,callback)
lst=[]
a=None
keepalive0=None
print 'ls',lst
</code>
I run it in python shell and in IDLE, both give me the same problem.
The output is:
'ls []'
I guess it's because the callback function is not called.
I want the <code>str()</code> object to be garbage collected and the output:
'ls []'


A:

If you want to store a reference to the list, store it in a global variable. <code>lst</code> is a reference else, so it is a local variable and by "re-assigning" a new list to it, you loose the reference.

